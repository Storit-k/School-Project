# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1092, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1092, 700))
        MainWindow.setMaximumSize(QSize(1092, 700))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #1e1e1e;\n"
"}\n"
".QWidget#sidebar_widget {\n"
"	background-color: #333333;\n"
"}\n"
"QWidget#sidebar_widget QPushButton {\n"
"	background-color: #333333;\n"
"	border: none;\n"
"	padding: 4;\n"
"}\n"
"QWidget#sidebar_widget QPushButton:hover {\n"
"	background-color: #3A3A3A;\n"
"}\n"
"QWidget#sidebar_widget QPushButton:clicked {\n"
"	background-color: rgb(197, 197, 197);\n"
"}\n"
"QWidget#row_buttons .QPushButton:disabled {\n"
"	background-color: #242424;\n"
"}\n"
"QWidget#add_widget QPushButton {\n"
"	background-color: #2D2D2D;\n"
"	border-color: #2D2D2D;\n"
"}\n"
"QWidget#add_widget QPushButton:hover {\n"
"	background-color: #3A3A3A;\n"
"}\n"
"QPlainTextEdit {\n"
"	border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1492, 824))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(70, 0, 1021, 701))
        font = QFont()
        font.setPointSize(9)
        self.stackedWidget.setFont(font)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.home_themes_table = QTableWidget(self.home_page)
        if (self.home_themes_table.columnCount() < 3):
            self.home_themes_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.home_themes_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.home_themes_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.home_themes_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.home_themes_table.rowCount() < 1):
            self.home_themes_table.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.home_themes_table.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.home_themes_table.setItem(0, 1, __qtablewidgetitem4)
        self.home_themes_table.setObjectName(u"home_themes_table")
        self.home_themes_table.setGeometry(QRect(50, 30, 741, 401))
        self.home_themes_table.setMinimumSize(QSize(741, 401))
        self.home_themes_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.home_themes_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.home_themes_table.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.home_themes_table.setGridStyle(Qt.PenStyle.NoPen)
        self.home_themes_table.setCornerButtonEnabled(True)
        self.home_themes_table.horizontalHeader().setVisible(True)
        self.home_themes_table.horizontalHeader().setCascadingSectionResizes(True)
        self.home_themes_table.horizontalHeader().setDefaultSectionSize(184)
        self.home_themes_table.horizontalHeader().setStretchLastSection(True)
        self.home_themes_table.verticalHeader().setVisible(False)
        self.row_buttons = QWidget(self.home_page)
        self.row_buttons.setObjectName(u"row_buttons")
        self.row_buttons.setGeometry(QRect(829, 80, 151, 331))
        self.row_buttons.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.row_buttons)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 141, 281))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.home_start_button = QPushButton(self.layoutWidget)
        self.home_start_button.setObjectName(u"home_start_button")
        self.home_start_button.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(11)
        self.home_start_button.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.home_start_button.setIcon(icon)
        self.home_start_button.setIconSize(QSize(17, 17))

        self.verticalLayout_2.addWidget(self.home_start_button)

        self.home_edit_button = QPushButton(self.layoutWidget)
        self.home_edit_button.setObjectName(u"home_edit_button")
        self.home_edit_button.setEnabled(False)
        self.home_edit_button.setFont(font1)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.home_edit_button.setIcon(icon1)
        self.home_edit_button.setIconSize(QSize(17, 17))

        self.verticalLayout_2.addWidget(self.home_edit_button)

        self.home_delete_button = QPushButton(self.layoutWidget)
        self.home_delete_button.setObjectName(u"home_delete_button")
        self.home_delete_button.setEnabled(False)
        self.home_delete_button.setFont(font1)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.home_delete_button.setIcon(icon2)
        self.home_delete_button.setIconSize(QSize(17, 17))

        self.verticalLayout_2.addWidget(self.home_delete_button)

        self.description_plain_text = QPlainTextEdit(self.home_page)
        self.description_plain_text.setObjectName(u"description_plain_text")
        self.description_plain_text.setGeometry(QRect(50, 500, 741, 121))
        self.description_plain_text.setStyleSheet(u"")
        self.description_plain_text.setReadOnly(False)
        self.description_label = QLabel(self.home_page)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setGeometry(QRect(50, 460, 191, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.description_label.setFont(font2)
        self.home_create_widget = QWidget(self.home_page)
        self.home_create_widget.setObjectName(u"home_create_widget")
        self.home_create_widget.setGeometry(QRect(743, 383, 48, 48))
        self.home_create_button = QPushButton(self.home_create_widget)
        self.home_create_button.setObjectName(u"home_create_button")
        self.home_create_button.setGeometry(QRect(0, 0, 48, 48))
        self.home_create_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/C:/Users/egork/Downloads/icons/create.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_create_button.setIcon(icon3)
        self.home_create_button.setIconSize(QSize(48, 48))
        self.save_description_button = QPushButton(self.home_page)
        self.save_description_button.setObjectName(u"save_description_button")
        self.save_description_button.setEnabled(False)
        self.save_description_button.setGeometry(QRect(290, 630, 231, 33))
        self.export_button = QPushButton(self.home_page)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setEnabled(False)
        self.export_button.setGeometry(QRect(743, 335, 48, 48))
        icon4 = QIcon()
        icon4.addFile(u":/icons/C:/Users/egork/Downloads/icons/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_button.setIcon(icon4)
        self.export_button.setIconSize(QSize(48, 48))
        self.stackedWidget.addWidget(self.home_page)
        self.train_page = QWidget()
        self.train_page.setObjectName(u"train_page")
        self.question_text_edit = QPlainTextEdit(self.train_page)
        self.question_text_edit.setObjectName(u"question_text_edit")
        self.question_text_edit.setGeometry(QRect(0, 50, 1021, 121))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(True)
        self.question_text_edit.setFont(font3)
        self.question_text_edit.setReadOnly(True)
        self.train_back_button = QPushButton(self.train_page)
        self.train_back_button.setObjectName(u"train_back_button")
        self.train_back_button.setGeometry(QRect(380, 650, 258, 39))
        sizePolicy.setHeightForWidth(self.train_back_button.sizePolicy().hasHeightForWidth())
        self.train_back_button.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(True)
        self.train_back_button.setFont(font4)
        self.line_4 = QFrame(self.train_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 620, 1021, 20))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget1 = QWidget(self.train_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 170, 1021, 321))
        self.answer_buttons_layout = QVBoxLayout(self.layoutWidget1)
        self.answer_buttons_layout.setObjectName(u"answer_buttons_layout")
        self.answer_buttons_layout.setContentsMargins(10, 0, 0, 0)
        self.answer_button_1 = QRadioButton(self.layoutWidget1)
        self.answer_button_1.setObjectName(u"answer_button_1")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        self.answer_button_1.setFont(font5)

        self.answer_buttons_layout.addWidget(self.answer_button_1)

        self.answer_button_2 = QRadioButton(self.layoutWidget1)
        self.answer_button_2.setObjectName(u"answer_button_2")
        self.answer_button_2.setFont(font5)

        self.answer_buttons_layout.addWidget(self.answer_button_2)

        self.answer_button_3 = QRadioButton(self.layoutWidget1)
        self.answer_button_3.setObjectName(u"answer_button_3")
        self.answer_button_3.setFont(font5)

        self.answer_buttons_layout.addWidget(self.answer_button_3)

        self.answer_button_4 = QRadioButton(self.layoutWidget1)
        self.answer_button_4.setObjectName(u"answer_button_4")
        self.answer_button_4.setFont(font5)

        self.answer_buttons_layout.addWidget(self.answer_button_4)

        self.layoutWidget2 = QWidget(self.train_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(160, 540, 691, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.train_answer_button = QPushButton(self.layoutWidget2)
        self.train_answer_button.setObjectName(u"train_answer_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.train_answer_button.sizePolicy().hasHeightForWidth())
        self.train_answer_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.train_answer_button)

        self.horizontalSpacer_5 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.train_next_button = QPushButton(self.layoutWidget2)
        self.train_next_button.setObjectName(u"train_next_button")
        self.train_next_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.train_next_button.sizePolicy().hasHeightForWidth())
        self.train_next_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.train_next_button)

        self.stackedWidget.addWidget(self.train_page)
        self.create_page = QWidget()
        self.create_page.setObjectName(u"create_page")
        self.create_themes_table = QTableWidget(self.create_page)
        if (self.create_themes_table.columnCount() < 2):
            self.create_themes_table.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.create_themes_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.create_themes_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.create_themes_table.setObjectName(u"create_themes_table")
        self.create_themes_table.setGeometry(QRect(50, 60, 922, 311))
        self.create_themes_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.create_themes_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.create_themes_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.create_themes_table.setGridStyle(Qt.PenStyle.NoPen)
        self.create_themes_table.horizontalHeader().setCascadingSectionResizes(True)
        self.create_themes_table.horizontalHeader().setDefaultSectionSize(460)
        self.create_themes_table.horizontalHeader().setStretchLastSection(True)
        self.create_themes_table.verticalHeader().setVisible(False)
        self.create_theme_lineedit = QLineEdit(self.create_page)
        self.create_theme_lineedit.setObjectName(u"create_theme_lineedit")
        self.create_theme_lineedit.setGeometry(QRect(90, 440, 370, 35))
        self.create_date_format = QComboBox(self.create_page)
        self.create_date_format.addItem("")
        self.create_date_format.addItem("")
        self.create_date_format.addItem("")
        self.create_date_format.setObjectName(u"create_date_format")
        self.create_date_format.setGeometry(QRect(640, 400, 260, 35))
        self.create_date_format.setFrame(True)
        self.layoutWidget_2 = QWidget(self.create_page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(180, 650, 631, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.create_back_button = QPushButton(self.layoutWidget_2)
        self.create_back_button.setObjectName(u"create_back_button")
        sizePolicy.setHeightForWidth(self.create_back_button.sizePolicy().hasHeightForWidth())
        self.create_back_button.setSizePolicy(sizePolicy)
        self.create_back_button.setFont(font4)

        self.horizontalLayout_3.addWidget(self.create_back_button)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.save_theme_button = QPushButton(self.layoutWidget_2)
        self.save_theme_button.setObjectName(u"save_theme_button")
        sizePolicy.setHeightForWidth(self.save_theme_button.sizePolicy().hasHeightForWidth())
        self.save_theme_button.setSizePolicy(sizePolicy)
        self.save_theme_button.setFont(font4)

        self.horizontalLayout_3.addWidget(self.save_theme_button)

        self.line = QFrame(self.create_page)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 620, 1021, 31))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget3 = QWidget(self.create_page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(180, 570, 631, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.create_create_button = QPushButton(self.layoutWidget3)
        self.create_create_button.setObjectName(u"create_create_button")
        sizePolicy.setHeightForWidth(self.create_create_button.sizePolicy().hasHeightForWidth())
        self.create_create_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.create_create_button)

        self.horizontalSpacer_3 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.create_edit_button = QPushButton(self.layoutWidget3)
        self.create_edit_button.setObjectName(u"create_edit_button")
        self.create_edit_button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.create_edit_button.sizePolicy().hasHeightForWidth())
        self.create_edit_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.create_edit_button)

        self.horizontalSpacer_4 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.create_delete_button = QPushButton(self.layoutWidget3)
        self.create_delete_button.setObjectName(u"create_delete_button")
        self.create_delete_button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.create_delete_button.sizePolicy().hasHeightForWidth())
        self.create_delete_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.create_delete_button)

        self.create_theme_name_lineedit = QLineEdit(self.create_page)
        self.create_theme_name_lineedit.setObjectName(u"create_theme_name_lineedit")
        self.create_theme_name_lineedit.setGeometry(QRect(180, 15, 641, 31))
        self.layoutWidget4 = QWidget(self.create_page)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(630, 460, 281, 71))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.layoutWidget4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.label_8 = QLabel(self.layoutWidget4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_8.addWidget(self.label_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.create_datetime_day = QSpinBox(self.layoutWidget4)
        self.create_datetime_day.setObjectName(u"create_datetime_day")
        self.create_datetime_day.setMinimum(1)
        self.create_datetime_day.setMaximum(31)

        self.horizontalLayout_7.addWidget(self.create_datetime_day)

        self.create_datetime_month = QSpinBox(self.layoutWidget4)
        self.create_datetime_month.setObjectName(u"create_datetime_month")
        self.create_datetime_month.setMinimum(1)
        self.create_datetime_month.setMaximum(12)

        self.horizontalLayout_7.addWidget(self.create_datetime_month)

        self.create_datetime_year = QSpinBox(self.layoutWidget4)
        self.create_datetime_year.setObjectName(u"create_datetime_year")
        self.create_datetime_year.setMinimum(1)
        self.create_datetime_year.setMaximum(9999)

        self.horizontalLayout_7.addWidget(self.create_datetime_year)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.import_button = QPushButton(self.create_page)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setGeometry(QRect(960, 647, 48, 48))
        icon5 = QIcon()
        icon5.addFile(u":/icons/C:/Users/egork/Downloads/icons/import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.import_button.setIcon(icon5)
        self.import_button.setIconSize(QSize(48, 48))
        self.stackedWidget.addWidget(self.create_page)
        self.edit_page = QWidget()
        self.edit_page.setObjectName(u"edit_page")
        self.edit_theme_lineedit = QLineEdit(self.edit_page)
        self.edit_theme_lineedit.setObjectName(u"edit_theme_lineedit")
        self.edit_theme_lineedit.setGeometry(QRect(90, 420, 370, 35))
        self.edit_themes_table = QTableWidget(self.edit_page)
        if (self.edit_themes_table.columnCount() < 2):
            self.edit_themes_table.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.edit_themes_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.edit_themes_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.edit_themes_table.setObjectName(u"edit_themes_table")
        self.edit_themes_table.setGeometry(QRect(50, 30, 922, 311))
        self.edit_themes_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.edit_themes_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.edit_themes_table.horizontalHeader().setDefaultSectionSize(460)
        self.edit_themes_table.horizontalHeader().setStretchLastSection(True)
        self.edit_themes_table.verticalHeader().setVisible(False)
        self.line_2 = QFrame(self.edit_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 610, 1021, 31))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.edit_date_format = QComboBox(self.edit_page)
        self.edit_date_format.addItem("")
        self.edit_date_format.addItem("")
        self.edit_date_format.addItem("")
        self.edit_date_format.setObjectName(u"edit_date_format")
        self.edit_date_format.setGeometry(QRect(640, 380, 260, 35))
        self.edit_date_format.setFrame(True)
        self.label_3 = QLabel(self.edit_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 640, 331, 51))
        font6 = QFont()
        font6.setItalic(True)
        self.label_3.setFont(font6)
        self.label_3.setWordWrap(True)
        self.edit_back_button = QPushButton(self.edit_page)
        self.edit_back_button.setObjectName(u"edit_back_button")
        self.edit_back_button.setGeometry(QRect(180, 640, 271, 41))
        sizePolicy.setHeightForWidth(self.edit_back_button.sizePolicy().hasHeightForWidth())
        self.edit_back_button.setSizePolicy(sizePolicy)
        self.edit_back_button.setFont(font4)
        self.layoutWidget_3 = QWidget(self.edit_page)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(630, 450, 281, 71))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.layoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_9.addWidget(self.label_10)

        self.label_11 = QLabel(self.layoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.label_12 = QLabel(self.layoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_9.addWidget(self.label_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.edit_datetime_day = QSpinBox(self.layoutWidget_3)
        self.edit_datetime_day.setObjectName(u"edit_datetime_day")
        self.edit_datetime_day.setMinimum(1)
        self.edit_datetime_day.setMaximum(31)

        self.horizontalLayout_10.addWidget(self.edit_datetime_day)

        self.edit_datetime_month = QSpinBox(self.layoutWidget_3)
        self.edit_datetime_month.setObjectName(u"edit_datetime_month")
        self.edit_datetime_month.setMinimum(1)
        self.edit_datetime_month.setMaximum(12)

        self.horizontalLayout_10.addWidget(self.edit_datetime_month)

        self.edit_datetime_year = QSpinBox(self.layoutWidget_3)
        self.edit_datetime_year.setObjectName(u"edit_datetime_year")
        self.edit_datetime_year.setMinimum(1)
        self.edit_datetime_year.setMaximum(9999)

        self.horizontalLayout_10.addWidget(self.edit_datetime_year)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.layoutWidget_4 = QWidget(self.edit_page)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(230, 560, 631, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.edit_create_button = QPushButton(self.layoutWidget_4)
        self.edit_create_button.setObjectName(u"edit_create_button")
        sizePolicy.setHeightForWidth(self.edit_create_button.sizePolicy().hasHeightForWidth())
        self.edit_create_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.edit_create_button)

        self.horizontalSpacer_8 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.edit_apply_button = QPushButton(self.layoutWidget_4)
        self.edit_apply_button.setObjectName(u"edit_apply_button")
        self.edit_apply_button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.edit_apply_button.sizePolicy().hasHeightForWidth())
        self.edit_apply_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.edit_apply_button)

        self.horizontalSpacer_9 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.edit_delete_button = QPushButton(self.layoutWidget_4)
        self.edit_delete_button.setObjectName(u"edit_delete_button")
        self.edit_delete_button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.edit_delete_button.sizePolicy().hasHeightForWidth())
        self.edit_delete_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.edit_delete_button)

        self.stackedWidget.addWidget(self.edit_page)
        self.delete_page = QWidget()
        self.delete_page.setObjectName(u"delete_page")
        self.layoutWidget_5 = QWidget(self.delete_page)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(160, 510, 691, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.delete_back_button = QPushButton(self.layoutWidget_5)
        self.delete_back_button.setObjectName(u"delete_back_button")
        sizePolicy.setHeightForWidth(self.delete_back_button.sizePolicy().hasHeightForWidth())
        self.delete_back_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.delete_back_button)

        self.horizontalSpacer_7 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.delete_delete_button = QPushButton(self.layoutWidget_5)
        self.delete_delete_button.setObjectName(u"delete_delete_button")
        sizePolicy.setHeightForWidth(self.delete_delete_button.sizePolicy().hasHeightForWidth())
        self.delete_delete_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.delete_delete_button)

        self.label_4 = QLabel(self.delete_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 120, 701, 151))
        font7 = QFont()
        font7.setFamilies([u"Source Code Pro"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_4.setFont(font7)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.delete_theme_textedit = QPlainTextEdit(self.delete_page)
        self.delete_theme_textedit.setObjectName(u"delete_theme_textedit")
        self.delete_theme_textedit.setGeometry(QRect(160, 320, 691, 75))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Historic"])
        font8.setPointSize(10)
        self.delete_theme_textedit.setFont(font8)
        self.delete_theme_textedit.setReadOnly(True)
        self.delete_theme_textedit.setBackgroundVisible(False)
        self.stackedWidget.addWidget(self.delete_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_5 = QLabel(self.settings_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 20, 1021, 71))
        font9 = QFont()
        font9.setPointSize(22)
        font9.setItalic(True)
        self.label_5.setFont(font9)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.settings_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 100, 1021, 31))
        font10 = QFont()
        font10.setPointSize(14)
        self.label_6.setFont(font10)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.settings_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 420, 1021, 31))
        self.label_13.setFont(font10)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_9 = QFrame(self.settings_page)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(0, 620, 1021, 21))
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.save_settings_button = QPushButton(self.settings_page)
        self.save_settings_button.setObjectName(u"save_settings_button")
        self.save_settings_button.setGeometry(QRect(400, 648, 221, 41))
        self.reset_settings_button = QPushButton(self.settings_page)
        self.reset_settings_button.setObjectName(u"reset_settings_button")
        self.reset_settings_button.setGeometry(QRect(30, 648, 141, 41))
        font11 = QFont()
        font11.setPointSize(8)
        font11.setBold(True)
        font11.setItalic(False)
        self.reset_settings_button.setFont(font11)
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRestore))
        self.reset_settings_button.setIcon(icon6)
        self.reset_settings_button.setIconSize(QSize(18, 18))
        self.layoutWidget5 = QWidget(self.settings_page)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(0, 140, 1031, 231))
        self.gridLayout = QGridLayout(self.layoutWidget5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(385, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(385, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 4, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(385, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 2, 0, 1, 1)

        self.line_6 = QFrame(self.layoutWidget5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_6, 0, 0, 1, 3)

        self.mix_external_events_checkbox = QCheckBox(self.layoutWidget5)
        self.mix_external_events_checkbox.setObjectName(u"mix_external_events_checkbox")

        self.gridLayout.addWidget(self.mix_external_events_checkbox, 4, 1, 1, 2)

        self.line_5 = QFrame(self.layoutWidget5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 5, 0, 1, 3)

        self.range_date_checkbox = QCheckBox(self.layoutWidget5)
        self.range_date_checkbox.setObjectName(u"range_date_checkbox")
        self.range_date_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.range_date_checkbox.setTristate(False)

        self.gridLayout.addWidget(self.range_date_checkbox, 1, 1, 1, 2)

        self.mix_external_date_checkbox = QCheckBox(self.layoutWidget5)
        self.mix_external_date_checkbox.setObjectName(u"mix_external_date_checkbox")

        self.gridLayout.addWidget(self.mix_external_date_checkbox, 3, 2, 1, 1)

        self.mix_date_checkbox = QCheckBox(self.layoutWidget5)
        self.mix_date_checkbox.setObjectName(u"mix_date_checkbox")

        self.gridLayout.addWidget(self.mix_date_checkbox, 2, 1, 1, 2)

        self.horizontalSpacer_10 = QSpacerItem(385, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 3, 0, 1, 1)

        self.label_16 = QLabel(self.layoutWidget5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.label_16, 3, 1, 1, 1)

        self.layoutWidget6 = QWidget(self.settings_page)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(0, 470, 1021, 81))
        self.gridLayout_2 = QGridLayout(self.layoutWidget6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.incorrect_hex_lineedit = QLineEdit(self.layoutWidget6)
        self.incorrect_hex_lineedit.setObjectName(u"incorrect_hex_lineedit")
        self.incorrect_hex_lineedit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout_2.addWidget(self.incorrect_hex_lineedit, 2, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 2, 3, 1, 1)

        self.correct_hex_lineedit = QLineEdit(self.layoutWidget6)
        self.correct_hex_lineedit.setObjectName(u"correct_hex_lineedit")
        self.correct_hex_lineedit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.correct_hex_lineedit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.correct_hex_lineedit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.correct_hex_lineedit, 1, 2, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 1, 3, 1, 1)

        self.label_14 = QLabel(self.layoutWidget6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 1, 1, 1, 1)

        self.line_7 = QFrame(self.layoutWidget6)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 0, 0, 1, 4)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_16, 2, 0, 1, 1)

        self.label_15 = QLabel(self.layoutWidget6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 2, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 1, 0, 1, 1)

        self.line_8 = QFrame(self.layoutWidget6)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 3, 0, 1, 4)

        self.stackedWidget.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.label_7 = QLabel(self.info_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 70, 1021, 81))
        font12 = QFont()
        font12.setPointSize(20)
        font12.setItalic(True)
        self.label_7.setFont(font12)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_17 = QLabel(self.info_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 580, 981, 91))
        font13 = QFont()
        font13.setFamilies([u"Calibri"])
        font13.setPointSize(12)
        self.label_17.setFont(font13)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_17.setWordWrap(True)
        self.label_18 = QLabel(self.info_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 290, 1021, 81))
        font14 = QFont()
        font14.setFamilies([u"Source Code Pro"])
        font14.setPointSize(16)
        font14.setBold(False)
        self.label_18.setFont(font14)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.info_page)
        self.sidebar_widget = QWidget(self.centralwidget)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        self.sidebar_widget.setGeometry(QRect(0, 0, 71, 700))
        self.sidebar_widget.setStyleSheet(u".QPushButton:clicked {\n"
"	background-color: #464646\n"
"}\n"
".QPushButton:checked {\n"
"	background-color: #464646\n"
"}")
        self.layoutWidget7 = QWidget(self.sidebar_widget)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(0, 10, 71, 50))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget7)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/C:/Users/egork/Downloads/icons/main.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.layoutWidget8 = QWidget(self.sidebar_widget)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(0, 60, 71, 641))
        self.verticalLayout = QVBoxLayout(self.layoutWidget8)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 20, 0, 10)
        self.home_button = QPushButton(self.layoutWidget8)
        self.home_button.setObjectName(u"home_button")
        sizePolicy.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy)
        icon7 = QIcon()
        icon7.addFile(u":/icons/C:/Users/egork/Downloads/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_button.setIcon(icon7)
        self.home_button.setIconSize(QSize(48, 48))
        self.home_button.setCheckable(True)
        self.home_button.setChecked(True)

        self.verticalLayout.addWidget(self.home_button)

        self.settings_button = QPushButton(self.layoutWidget8)
        self.settings_button.setObjectName(u"settings_button")
        icon8 = QIcon()
        icon8.addFile(u":/icons/C:/Users/egork/Downloads/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_button.setIcon(icon8)
        self.settings_button.setIconSize(QSize(48, 48))
        self.settings_button.setCheckable(True)

        self.verticalLayout.addWidget(self.settings_button)

        self.info_button = QPushButton(self.layoutWidget8)
        self.info_button.setObjectName(u"info_button")
        icon9 = QIcon()
        icon9.addFile(u":/icons/C:/Users/egork/Downloads/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_button.setIcon(icon9)
        self.info_button.setIconSize(QSize(48, 48))
        self.info_button.setCheckable(True)

        self.verticalLayout.addWidget(self.info_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.exit_button = QPushButton(self.layoutWidget8)
        self.exit_button.setObjectName(u"exit_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/C:/Users/egork/Downloads/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_button.setIcon(icon10)
        self.exit_button.setIconSize(QSize(48, 48))

        self.verticalLayout.addWidget(self.exit_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_button.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # __init__

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.home_themes_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.home_themes_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u0439", None));
        ___qtablewidgetitem2 = self.home_themes_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));

        __sortingEnabled = self.home_themes_table.isSortingEnabled()
        self.home_themes_table.setSortingEnabled(False)
        self.home_themes_table.setSortingEnabled(__sortingEnabled)

        self.home_start_button.setText(QCoreApplication.translate("MainWindow", u" \u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.home_edit_button.setText(QCoreApplication.translate("MainWindow", u" \u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.home_delete_button.setText(QCoreApplication.translate("MainWindow", u" \u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.home_create_button.setText("")
        self.save_description_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.export_button.setText("")
        self.question_text_edit.setPlainText(QCoreApplication.translate("MainWindow", u"Task here", None))
        self.question_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task here", None))
        self.train_back_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.answer_button_1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.answer_button_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.answer_button_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.answer_button_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.train_answer_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442\u0438\u0442\u044c", None))
        self.train_next_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        ___qtablewidgetitem3 = self.create_themes_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u0435", None));
        ___qtablewidgetitem4 = self.create_themes_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        self.create_theme_lineedit.setInputMask("")
        self.create_theme_lineedit.setText("")
        self.create_theme_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u0435: ", None))
        self.create_date_format.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434, \u043c\u0435\u0441\u044f\u0446, \u0447\u0438\u0441\u043b\u043e", None))
        self.create_date_format.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0438 \u043c\u0435\u0441\u044f\u0446", None))
        self.create_date_format.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))

        self.create_back_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.save_theme_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
        self.create_create_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.create_edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.create_delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.create_theme_name_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043c\u044b:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))
        self.import_button.setText("")
        self.edit_theme_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u0435: ", None))
        ___qtablewidgetitem5 = self.edit_themes_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u044b\u0442\u0438\u0435", None));
        ___qtablewidgetitem6 = self.edit_themes_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        self.edit_date_format.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434, \u043c\u0435\u0441\u044f\u0446, \u0447\u0438\u0441\u043b\u043e", None))
        self.edit_date_format.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0438 \u043c\u0435\u0441\u044f\u0446", None))
        self.edit_date_format.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"*\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u044e\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.edit_back_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))
        self.edit_create_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.edit_apply_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.edit_delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.delete_back_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.delete_delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435! \u0412\u044b \u0441\u043e\u0431\u0438\u0440\u0430\u0435\u0442\u0435\u0441\u044c \u0443\u0434\u0430\u043b\u0442\u044c \u0442\u0435\u043c\u0443, \u044d\u0442\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043d\u0435\u043b\u044c\u0437\u044f \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043c\u0435\u043d\u0438\u0442\u044c! \u0412\u044b \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c?", None))
        self.delete_theme_textedit.setDocumentTitle("")
        self.delete_theme_textedit.setPlainText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u043e\u0432", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u0430", None))
        self.save_settings_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.reset_settings_button.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.mix_external_events_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0438\u0437 \u0434\u0440\u0443\u0433\u0438\u0445 \u0442\u0435\u043c", None))
        self.range_date_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0434\u0430\u0442", None))
        self.mix_external_date_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u0442\u044b \u0438\u0437 \u0434\u0440\u0443\u0433\u0438\u0445 \u0442\u0435\u043c", None))
        self.mix_date_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0451\u043d\u043d\u044b\u0435 \u0434\u0430\u0442\u044b", None))
        self.label_16.setText("")
        self.incorrect_hex_lineedit.setInputMask(QCoreApplication.translate("MainWindow", u"\\#<HHHHHH", None))
        self.correct_hex_lineedit.setInputMask(QCoreApplication.translate("MainWindow", u"\\#<HHHHHH", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0443\u0447\u0430\u0449\u0438\u043c\u0441\u044f 10\u0444\u043c\u00b9 \u043a\u043b\u0430\u0441\u0441\u0430 \u041a\u043e\u0441\u0442\u0440\u043e\u043c\u0441\u043a\u0438\u043c \u0415. \u0410.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f: 0.1 (beta)", None))
        self.label.setText("")
        self.home_button.setText("")
        self.settings_button.setText("")
        self.info_button.setText("")
        self.exit_button.setText("")
    # retranslateUi

