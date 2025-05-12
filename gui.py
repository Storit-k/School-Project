from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QFileDialog
from task_gen import Combinator, Task
from form import Ui_MainWindow
from database import Database
from pathlib import Path
import base64 as b64
import json
import os


class GUI(QMainWindow):
    def __init__(self, db: Database):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow(self)

        self.previous_index = 0
        self.database = db

        # --- SIDEBAR ---
        self.ui.home_button.clicked.connect(lambda: self.side_button_clicked('home'))
        self.ui.settings_button.clicked.connect(lambda: self.side_button_clicked('settings'))
        self.ui.info_button.clicked.connect(lambda: self.side_button_clicked('info'))

        # --- HOME PAGE ---
        self.ui.home_start_button.clicked.connect(lambda: self.home_button_clicked('start'))
        self.ui.home_create_button.clicked.connect(lambda: self.home_button_clicked('create'))
        self.ui.home_edit_button.clicked.connect(lambda: self.home_button_clicked('edit'))
        self.ui.home_delete_button.clicked.connect(lambda: self.home_button_clicked('delete'))

        self.ui.home_themes_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.home_themes_table.itemSelectionChanged.connect(lambda: (self.home_switch_buttons(state=1),
                                                                        self.update_description()))
        self.indexes_comp = {}
        self.home_display_themes()

        self.ui.export_button.clicked.connect(self.export_theme)

        self.ui.description_plain_text.textChanged.connect(lambda: self.ui.save_description_button.setEnabled(True))
        self.ui.save_description_button.clicked.connect(self.save_description)

        # --- DELETE THEME PAGE ---
        self.ui.delete_back_button.clicked.connect(self.home)
        self.ui.delete_delete_button.clicked.connect(self.delete_theme)

        # --- EDIT THEME PAGE ---
        self.ui.edit_back_button.clicked.connect(lambda: (self.edit_update_theme_name(), self.home(reload=True)))
        self.ui.edit_delete_button.clicked.connect(self.edit_delete_event)
        self.ui.edit_apply_button.clicked.connect(self.edit_change_event)
        self.ui.edit_create_button.clicked.connect(self.edit_add_event)

        self.ui.edit_themes_table.currentItemChanged.connect(self.edit_fields_update)
        self.edit_indexes_comp = {}

        self.ui.edit_date_format.setItemData(0, 'dmy')
        self.ui.edit_date_format.setItemData(1, 'my')
        self.ui.edit_date_format.setItemData(2, 'y')
        self.ui.edit_date_format.currentIndexChanged.connect(lambda: self.change_datetime_format('edit'))

        # --- CREATE THEME PAGE ---
        self.ui.create_back_button.clicked.connect(self.home)
        self.ui.create_delete_button.clicked.connect(self.create_delete_event)
        self.ui.create_create_button.clicked.connect(self.create_add_event)
        self.ui.create_edit_button.clicked.connect(self.create_edit_event)
        self.ui.save_theme_button.clicked.connect(self.create_save_theme)

        self.ui.create_date_format.setItemData(0, 'dmy')
        self.ui.create_date_format.setItemData(1, 'my')
        self.ui.create_date_format.setItemData(2, 'y')
        self.ui.create_date_format.currentIndexChanged.connect(lambda: self.change_datetime_format('create'))

        self.ui.import_button.clicked.connect(self.import_theme)

        # --- TRAINING PAGE ---
        self.ui.train_answer_button.clicked.connect(self.train_answer)
        self.ui.train_next_button.clicked.connect(self.train_next_question)
        self.ui.train_back_button.clicked.connect(self.home)

        self.combinator: Combinator | None = None
        self.current_task: Task | None = None

        # --- SETTINGS PAGE ---
        settings = self.database.get_settings()
        self.correct_color = settings['correct_color']
        self.incorrect_color = settings['incorrect_color']

        self.ui.range_date_checkbox.stateChanged.connect(self.settings_date_check_toggled)
        self.ui.mix_date_checkbox.stateChanged.connect(self.settings_date_check_toggled)
        self.ui.mix_external_date_checkbox.stateChanged.connect(self.settings_date_check_toggled)
        self.ui.save_settings_button.clicked.connect(self.save_settings)
        self.ui.reset_settings_button.clicked.connect(self.reset_settings)

    def home(self, reload: bool = False):
        if reload:
            self.home_display_themes()
            self.ui.description_plain_text.clear()

        self.previous_index = 0
        self.ui.stackedWidget.setCurrentIndex(0)

    def side_button_clicked(self, target: str):
        self.ui.home_button.setChecked(False)
        self.ui.settings_button.setChecked(False)
        self.ui.info_button.setChecked(False)

        match target:
            case 'home':
                if self.ui.stackedWidget.currentIndex() in (5, 6):
                    self.ui.stackedWidget.setCurrentIndex(self.previous_index)

                self.ui.home_button.setChecked(True)

            case 'settings':
                index = self.ui.stackedWidget.currentIndex()
                if index not in (5, 6):
                    self.previous_index = index

                self.ui.stackedWidget.setCurrentIndex(5)
                self.load_settings()

                self.ui.settings_button.setChecked(True)

            case 'info':
                index = self.ui.stackedWidget.currentIndex()
                if index not in (5, 6):
                    self.previous_index = index

                self.ui.stackedWidget.setCurrentIndex(6)

                self.ui.info_button.setChecked(True)

            case _:
                pass

    def home_display_themes(self):
        themes = self.database.get_themes()

        self.ui.home_themes_table.setRowCount(0)  # Clear the table
        self.indexes_comp.clear()

        for row, (indx, theme, date, amount) in enumerate(themes):
            self.ui.home_themes_table.insertRow(row)
            self.indexes_comp[row] = indx
            self.ui.home_themes_table.setItem(row, 0, QTableWidgetItem(theme))
            self.ui.home_themes_table.setItem(row, 2, QTableWidgetItem(date))
            self.ui.home_themes_table.setItem(row, 1, QTableWidgetItem(str(amount)))

    def home_switch_buttons(self, state: int):
        if state and self.ui.home_themes_table.item(self.ui.home_themes_table.currentRow(), 1):
            if int(self.ui.home_themes_table.item(self.ui.home_themes_table.currentRow(), 1).text()) >= 4:
                self.ui.home_start_button.setEnabled(True)
            else:
                self.ui.home_start_button.setEnabled(False)

            self.ui.home_edit_button.setEnabled(True)
            self.ui.home_delete_button.setEnabled(True)
            self.ui.export_button.setEnabled(True)
        else:
            self.ui.home_start_button.setEnabled(False)
            self.ui.home_edit_button.setEnabled(False)
            self.ui.home_delete_button.setEnabled(False)
            self.ui.export_button.setEnabled(False)

    def home_button_clicked(self, target: str):
        match target:
            case 'start':
                self.ui.stackedWidget.setCurrentIndex(1)
                self.combinator = Combinator(self.database, self.indexes_comp[self.ui.home_themes_table.currentRow()])
                self.train_next_question()

            case 'create':
                self.ui.stackedWidget.setCurrentIndex(2)

            case 'edit':
                self.ui.edit_theme_name_lineedit.clear()
                title = self.ui.home_themes_table.item(self.ui.home_themes_table.currentRow(), 0).text()
                self.ui.edit_theme_name_lineedit.insert(title)

                self.ui.stackedWidget.setCurrentIndex(3)
                self.edit_update_events()

            case 'delete':
                self.ui.stackedWidget.setCurrentIndex(4)
                self.ui.delete_theme_textedit.clear()
                theme_name = self.ui.home_themes_table.item(self.ui.home_themes_table.currentIndex().row(), 0).text()
                self.ui.delete_theme_textedit.insertPlainText(f'\nТема: {theme_name}')

            case _:
                pass

    def change_datetime_format(self, target: str):
        getattr(self.ui, f'{target}_datetime_day').setEnabled(False)
        getattr(self.ui, f'{target}_datetime_month').setEnabled(False)

        dis_format = getattr(self.ui, f'{target}_date_format').currentData()
        if 'm' in dis_format:
            getattr(self.ui, f'{target}_datetime_month').setEnabled(True)
        if 'd' in dis_format:
            getattr(self.ui, f'{target}_datetime_day').setEnabled(True)

    def create_add_event(self, parse: bool = False):
        event = self.ui.create_theme_lineedit.text()
        date = ''
        date_widgets = [self.ui.create_datetime_day, self.ui.create_datetime_month, self.ui.create_datetime_year]

        for i, widget in enumerate(date_widgets):
            if widget.isEnabled():
                if i < 2:
                    date += f'{widget.text():>02}.'
                else:
                    date += f'{widget.text():>04}'

        if not event or parse:
            return event, date

        indx = self.ui.create_themes_table.rowCount()
        self.ui.create_themes_table.insertRow(indx)
        self.ui.create_themes_table.setItem(indx, 0, QTableWidgetItem(event))
        self.ui.create_themes_table.setItem(indx, 1, QTableWidgetItem(date))
        self.ui.create_themes_table.selectRow(indx)

        self.ui.create_edit_button.setEnabled(True)
        self.ui.create_delete_button.setEnabled(True)

        self.ui.create_theme_lineedit.clear()

    def create_edit_event(self):
        event, date = self.create_add_event(parse=True)

        if not event:
            return

        indx = self.ui.create_themes_table.currentIndex().row()
        self.ui.create_themes_table.setItem(indx, 0, QTableWidgetItem(event))
        self.ui.create_themes_table.setItem(indx, 1, QTableWidgetItem(date))

    def create_delete_event(self):
        self.ui.create_themes_table.removeRow(self.ui.create_themes_table.currentIndex().row())

    def create_save_theme(self):
        theme = {}

        name = self.ui.create_theme_name_lineedit.text()
        events = []

        for row in range(self.ui.create_themes_table.rowCount()):
            t = {}
            event = self.ui.create_themes_table.item(row, 0).text()
            date = self.ui.create_themes_table.item(row, 1).text()
            t['event'] = event

            match date.split('.'):
                case [year]:
                    t['date'] = {'day': None, 'month': None, 'year': year}
                case [month, year]:
                    t['date'] = {'day': None, 'month': month, 'year': year}
                case [day, month, year]:
                    t['date'] = {'day': day, 'month': month, 'year': year}

            events.append(t)

        if name and events:
            theme['name'] = name
            theme['events'] = events
            self.database.add_theme(theme)
            self.home(reload=True)
            self.ui.create_themes_table.setRowCount(0)
            self.ui.create_theme_lineedit.clear()
            self.ui.create_theme_name_lineedit.clear()
            self.ui.create_edit_button.setEnabled(False)
            self.ui.create_delete_button.setEnabled(False)
        else:
            return

    def edit_update_events(self):
        prev_index = self.ui.edit_themes_table.currentRow()
        if not prev_index:
            prev_index = 0

        self.ui.edit_themes_table.setRowCount(0)

        theme_id = self.indexes_comp[self.ui.home_themes_table.currentRow()]
        events = self.database.get_events_by_theme(theme_id)

        for i, event in enumerate(events):
            self.ui.edit_themes_table.insertRow(i)
            self.ui.edit_themes_table.setItem(i, 0, QTableWidgetItem(event['event']))
            self.edit_indexes_comp[i] = event['id']

            date = ''
            match event['date']:
                case {'day': None, 'month': None, 'year': year}:
                    date = f'{year:>04}'
                case {'day': None, 'month': month, 'year': year}:
                    date = f'{month:>02}.{year:>04}'
                case {'day': day, 'month': month, 'year': year}:
                    date = f'{day:>02}.{month:>02}.{year:>04}'

            self.ui.edit_themes_table.setItem(i, 1, QTableWidgetItem(date))

        if self.ui.edit_themes_table.rowCount() >= prev_index:
            self.ui.edit_themes_table.selectRow(prev_index)
        elif prev_index != 0:
            self.ui.edit_themes_table.selectRow(prev_index - 1)

    def edit_fields_update(self):
        row = self.ui.edit_themes_table.currentRow()
        self.ui.edit_theme_lineedit.setText(self.ui.edit_themes_table.item(row, 0).text())

        match [int(i) for i in self.ui.edit_themes_table.item(row, 1).text().split('.')]:
            case [day, month, year]:
                self.ui.edit_date_format.setCurrentIndex(0)
                self.ui.edit_datetime_day.setValue(day)
                self.ui.edit_datetime_month.setValue(month)
                self.ui.edit_datetime_year.setValue(year)
            case [month, year]:
                self.ui.edit_date_format.setCurrentIndex(1)
                self.ui.edit_datetime_month.setValue(month)
                self.ui.edit_datetime_year.setValue(year)
            case [year]:
                self.ui.edit_date_format.setCurrentIndex(2)
                self.ui.edit_datetime_year.setValue(year)

        self.ui.edit_apply_button.setEnabled(True)
        self.ui.edit_delete_button.setEnabled(True)

    def edit_add_event(self, parse: bool = False):
        event = self.ui.edit_theme_lineedit.text()
        date = {'day': None, 'month': None, 'year': None}
        date_widgets = [self.ui.edit_datetime_day, self.ui.edit_datetime_month, self.ui.edit_datetime_year]

        for key, widget in zip(date.keys(), date_widgets):
            if widget.isEnabled():
                date[key] = widget.text()

        if not event or parse:
            return event, date

        event = {'event': event, 'date': date}
        theme_id = self.indexes_comp[self.ui.home_themes_table.currentRow()]
        self.database.add_event(theme_id, event)
        self.edit_update_events()

    def edit_change_event(self):
        event_id = self.edit_indexes_comp[self.ui.edit_themes_table.currentRow()]
        event, date = self.edit_add_event(parse=True)

        if not event:
            return

        self.database.update_event(event_id, {'event': event, 'date': date})
        self.edit_update_events()

    def edit_delete_event(self):
        event_id = self.edit_indexes_comp[self.ui.edit_themes_table.currentRow()]
        self.database.remove_event(event_id)
        self.edit_update_events()

    def edit_update_theme_name(self):
        new_title = self.ui.edit_theme_name_lineedit.text()
        current_title = self.ui.home_themes_table.item(self.ui.home_themes_table.currentRow(), 0).text()
        if (new_title != current_title) and new_title.split():
            theme_id = self.indexes_comp[self.ui.home_themes_table.currentRow()]
            self.database.rename_theme(theme_id, new_title)


    def delete_theme(self):
        theme_id = self.indexes_comp[self.ui.home_themes_table.currentIndex().row()]
        self.database.remove_theme(theme_id)
        self.home_switch_buttons(state=0)
        self.home(reload=True)

    def train_next_question(self):
        self.current_task = self.combinator.generate_task()
        q = self.current_task()
        question, answers = q['question'], q['answers']
        answ_buttons = [self.ui.answer_button_1, self.ui.answer_button_2, self.ui.answer_button_3,
                        self.ui.answer_button_4]

        self.ui.question_text_edit.clear()
        if self.current_task.is_date_task:
            self.ui.question_text_edit.insertPlainText(f'Выберите, что произошло в указанную дату:\n\n{question}')
        else:
            self.ui.question_text_edit.insertPlainText(f'Выберите, когда произошло следующее событие:\n\n{question}')

        answ_buttons[0].setChecked(True)
        for i, button in enumerate(answ_buttons):
            button.setText(answers[i])
            button.setStyleSheet('color: white')

        self.ui.train_next_button.setEnabled(False)
        self.ui.train_answer_button.setEnabled(True)

    def train_answer(self):
        answ_buttons = [self.ui.answer_button_1, self.ui.answer_button_2, self.ui.answer_button_3,
                        self.ui.answer_button_4]

        answer_button = None
        answer = ''
        correct_answer = self.current_task(get_answer=True)
        for button in answ_buttons:
            if button.isChecked():
                answer_button = button
                answer = button.text()

        if answer == correct_answer:
            answer_button.setStyleSheet(f'color: {self.correct_color}')
        else:
            answer_button.setStyleSheet(f'color: {self.incorrect_color}')
            for button in answ_buttons:
                if button.text() == correct_answer:
                    button.setStyleSheet(f'color: {self.correct_color}')

        self.ui.train_answer_button.setEnabled(False)
        self.ui.train_next_button.setEnabled(True)

    def settings_date_check_toggled(self):

        if self.ui.mix_date_checkbox.isChecked():
            self.ui.mix_external_date_checkbox.setEnabled(True)
        else:
            self.ui.mix_external_date_checkbox.setChecked(False)
            self.ui.mix_external_date_checkbox.setEnabled(False)

        if not self.ui.range_date_checkbox.isChecked():
            self.ui.range_date_checkbox.setEnabled(True)
            self.ui.mix_date_checkbox.setEnabled(False)
        elif not self.ui.mix_date_checkbox.isChecked():
            self.ui.mix_date_checkbox.setEnabled(True)
            self.ui.range_date_checkbox.setEnabled(False)
        else:
            self.ui.range_date_checkbox.setEnabled(True)
            self.ui.mix_date_checkbox.setEnabled(True)

    def load_settings(self):
        match self.database.get_settings():
            case {'use_months_names': umn, 'range_dates': rd, 'mix_dates': md, 'mix_external_dates': med,
                  'mix_external_events': mee, 'correct_color': correct_hex, 'incorrect_color': incorrect_hex}:
                self.ui.use_monts_names.setChecked(bool(umn))
                self.ui.range_date_checkbox.setChecked(bool(rd))
                self.ui.mix_date_checkbox.setChecked(bool(md))
                self.ui.mix_external_date_checkbox.setEnabled(bool(md))
                self.ui.mix_external_date_checkbox.setChecked(bool(med))
                self.ui.mix_external_events_checkbox.setChecked(bool(mee))

                self.ui.correct_hex_lineedit.clear()
                self.ui.correct_hex_lineedit.insert(correct_hex)
                self.ui.incorrect_hex_lineedit.clear()
                self.ui.incorrect_hex_lineedit.insert(incorrect_hex)

    def save_settings(self):
        settings = {
            'use_months_names': int(self.ui.use_monts_names.isChecked()),
            'range_dates': int(self.ui.range_date_checkbox.isChecked()),
            'mix_dates': int(self.ui.mix_date_checkbox.isChecked()),
            'mix_external_dates': int(self.ui.mix_external_date_checkbox.isChecked()),
            'mix_external_events': int(self.ui.mix_external_events_checkbox.isChecked()),
            'correct_color': self.ui.correct_hex_lineedit.text(),
            'incorrect_color': self.ui.incorrect_hex_lineedit.text()
        }

        self.correct_color = settings['correct_color']
        self.incorrect_color = settings['incorrect_color']

        self.database.update_settings(settings)

    def reset_settings(self):
        self.database.reset_settings()
        self.load_settings()

    def export_theme(self):
        theme_id = self.indexes_comp[self.ui.home_themes_table.currentRow()]

        theme = self.database.get_full_theme(theme_id)
        description = self.database.get_description(theme_id)
        date = self.ui.home_themes_table.item(self.ui.home_themes_table.currentRow(), 2).text()

        export_data = {'theme': theme, 'description': description, 'datetime': date}

        downloads = Path('C:/Users', os.getlogin(), 'Downloads', theme['name'] + '.tef')

        filename = QFileDialog.getSaveFileName(self, 'Export Theme', f'{downloads}',
                                               'Theme Export File (*.tef)')
        if filename[0]:
            Path(filename[0]).write_bytes(b64.b85encode(json.dumps(export_data).encode()))

    def import_theme(self):
        downloads = Path('C:/Users', os.getlogin(), 'Downloads')
        filenames = QFileDialog.getOpenFileNames(self, 'Import Theme', f'{downloads}',
                                               'Theme Export File (*.tef)')
        if filenames[0]:
            for file in filenames[0]:
                data = Path(file).read_bytes()
                import_data = json.loads(b64.b85decode(data).decode())

                self.database.import_theme(import_data)

            self.home(reload=True)
            self.ui.create_themes_table.setRowCount(0)
            self.ui.create_theme_lineedit.clear()
            self.ui.create_theme_name_lineedit.clear()
            self.ui.create_edit_button.setEnabled(False)
            self.ui.create_delete_button.setEnabled(False)

    def update_description(self):
        if self.ui.home_themes_table.currentRow() >= 0:
            theme_id = self.indexes_comp[self.ui.home_themes_table.currentRow()]
            description = self.database.get_description(theme_id)

            self.ui.description_plain_text.clear()
            self.ui.description_plain_text.insertPlainText(description)
            self.ui.save_description_button.setEnabled(False)

    def save_description(self):
        theme_id = self.indexes_comp[self.ui.home_themes_table.currentRow()]
        description = self.ui.description_plain_text.toPlainText()
        self.database.update_description(theme_id, description)
        self.ui.save_description_button.setEnabled(False)
