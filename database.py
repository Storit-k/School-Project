from sqlite3 import Connection, Cursor
from pathlib import Path
import time


class Database(Connection):
    def __init__(self, db_file: str | Path):
        super().__init__(db_file)

        self.cursor: Cursor = self.cursor()

        self.cursor.execute("PRAGMA foreign_keys = ON;")

        self.__create_tables()

    def __create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Themes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            theme TEXT NOT NULL,
            creation_date TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Descriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            theme_id INTEGER NOT NULL,
            FOREIGN KEY (theme_id) REFERENCES Themes (id) ON DELETE CASCADE
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            theme_id INTEGER NOT NULL,
            date_id INTEGER NOT NULL,
            event TEXT NOT NULL,
            FOREIGN KEY (theme_id) REFERENCES Themes (id) ON DELETE CASCADE
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Dates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year TEXT NOT NULL,
            month TEXT DEFAULT NULL,
            day TEXT DEFAULT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            use_months_names INTEGER NOT NULL DEFAULT 0,
            range_dates INTEGER NOT NULL DEFAULT 1,
            mix_dates INTEGER NOT NULL DEFAULT 1,
            mix_external_dates INTEGER NOT NULL DEFAULT 1,
            mix_external_events INTEGER NOT NULL DEFAULT 0,
            correct_color TEXT NOT NULL DEFAULT '#298f01',
            incorrect_color TEXT NOT NULL DEFAULT '#bd0202'
            )
        """)

        self.cursor.execute("""
            SELECT * FROM Settings WHERE id = 1
        """)
        res = self.cursor.fetchone()
        if res is None:
            self.cursor.execute("""
                INSERT INTO Settings(id) VALUES (1)
            """)

        self.commit()

    def __get_date_id(self, formatted_date: tuple[str, str | None, str | None]):
        self.cursor.execute("""
            SELECT id FROM Dates WHERE year=? AND month=? AND day=?
        """, formatted_date)

        if i := self.cursor.fetchone():
            date_id = i[0]
        else:
            self.cursor.execute("""
                INSERT INTO Dates(year, month, day) VALUES (?, ?, ?)
            """, formatted_date)
            date_id = self.cursor.lastrowid

        return date_id

    def add_theme(self, theme: dict[str:str, str:list[dict]]):
        self.cursor.execute("""
            INSERT INTO Themes(theme, creation_date) VALUES (?, ?)
        """, (theme['name'], time.strftime("%d-%m-%Y %H:%M")))

        theme_id: int = self.cursor.lastrowid
        for event in theme['events']:

            date = format_date_dict(event['date'])
            date_id = self.__get_date_id(date)

            self.cursor.execute("""
                INSERT INTO Events(theme_id, date_id, event) VALUES (?, ?, ?)
            """, (theme_id, date_id, event['event']))

        self.commit()

    def import_theme(self, import_data: dict):
        theme, description, datetime = import_data['theme'], import_data['description'], import_data['datetime']

        self.add_theme(theme)

        self.cursor.execute("SELECT id FROM Themes WHERE theme=?", (theme['name'],))
        theme_id = self.cursor.fetchall()[-1][0]

        self.update_description(theme_id, description)
        self.cursor.execute("UPDATE Themes SET creation_date=? WHERE id=?", (datetime, theme_id))

        self.commit()

    def rename_theme(self, theme_id: int, new_title: str):
        self.cursor.execute("""
        UPDATE Themes
        SET theme=?
        WHERE id=?
        """, (new_title, theme_id))

        self.commit()

    def remove_theme(self, theme_id: int):
        self.cursor.execute("""
            DELETE FROM Themes WHERE id=?
        """, (theme_id,))

        self.commit()

    def get_full_theme(self, theme_id: int):
        self.cursor.execute("""
            SELECT t.theme, d.year, d.month, d.day, e.event
            FROM Themes t
            JOIN Events e ON t.id = e.theme_id
            JOIN Dates d ON e.date_id = d.id
            WHERE t.id =?
        """, (theme_id,))

        theme_data = self.cursor.fetchall()
        theme = {
            'name': theme_data[0][0],
            'events': []
        }
        for _, year, month, day, event in theme_data:
            theme['events'].append({
                'date': date_from_formatted((year, month, day)),
                'event': event
            })

        return theme

    def add_event(self, theme_id: int, event: dict[str: str, str: dict]):
        date = format_date_dict(event['date'])
        date_id = self.__get_date_id(date)

        self.cursor.execute("""
            INSERT INTO Events(theme_id, date_id, event) VALUES (?, ?, ?)
        """, (theme_id, date_id, event['event']))

        self.commit()

    def update_event(self, event_id, event: dict[str: str, str:dict]):
        date = format_date_dict(event['date'])
        date_id = self.__get_date_id(date)
        self.cursor.execute("""
            UPDATE Events
            SET date_id=?, event=?
            WHERE id=?
        """, (date_id, event['event'], event_id))

        self.commit()

    def remove_event(self, event_id: int):
        self.cursor.execute("""
            DELETE FROM Events WHERE id=?
        """, (event_id,))

        self.commit()

    def get_themes(self):
        self.cursor.execute("""
            SELECT * FROM Themes
        """)

        themes = []
        themes_data = self.cursor.fetchall()
        for id, theme, date in themes_data:
            self.cursor.execute("""
                SELECT id FROM Events WHERE theme_id = ?
            """, (id,))
            themes.append((id, theme, date, len(self.cursor.fetchall())))

        return themes

    def get_events_by_theme(self, theme_id: int):
        self.cursor.execute("""
            SELECT * FROM Events WHERE theme_id = ?
        """, (theme_id,))

        events = []
        events_data = self.cursor.fetchall()
        for id, _, date_id, event in events_data:
            self.cursor.execute("""
                SELECT year, month, day FROM Dates WHERE id = ?
            """, (date_id,))
            struct_date = self.cursor.fetchone()
            date = date_from_formatted(struct_date)

            events.append({'id': id, 'event': event, 'date': date})

        return events

    def get_random_dates(self, pattern_date: dict):
        date = format_date_dict(pattern_date.copy())

        self.cursor.execute("""
            SELECT year, month, day FROM Dates WHERE year!=? OR month!=? OR day!=? ORDER BY random()
        """, date)

        res = []
        rows = self.cursor.fetchall()

        if len(rows) >= 3:
            for i in range(3):
                res.append(date_from_formatted(rows[i]))
            return res

    def get_random_events(self, exclude_event: str):
        self.cursor.execute("""
            SELECT event FROM Events WHERE event!=? ORDER BY random()
        """, (exclude_event,))

        rows = self.cursor.fetchall()
        res = [rows[i][0] for i in range(3)]

        return res

    def get_settings(self):
        self.cursor.execute("""
            SELECT * FROM Settings
        """)

        settings = self.cursor.fetchone()

        try:
            return {
                'use_months_names': settings[1],
                'range_dates': settings[2],
                'mix_dates': settings[3],
                'mix_external_dates': settings[4],
                'mix_external_events': settings[5],
                'correct_color': settings[6],
                'incorrect_color': settings[7]
            }
        except IndexError:
            self.reset_settings()
            return self.get_settings()

    def update_settings(self, settings: dict):
        self.cursor.execute("""
            UPDATE Settings
            SET use_months_names=?, range_dates=?, mix_dates=?, mix_external_dates=?, mix_external_events=?, correct_color=?, incorrect_color=?
            WHERE id=1
        """, (
            settings['use_months_names'],
            settings['range_dates'],
            settings['mix_dates'],
            settings['mix_external_dates'],
            settings['mix_external_events'],
            settings['correct_color'],
            settings['incorrect_color']
        ))

        self.commit()

    def reset_settings(self):
        self.cursor.execute("""
            DROP TABLE Settings
        """)
        self.__create_tables()
        self.cursor.execute("""
            INSERT INTO Settings(use_months_names) VALUES (0)
        """)

        self.commit()

    def update_description(self, theme_id: int, description: str):
        self.cursor.execute("SELECT id FROM Descriptions WHERE theme_id=?", (theme_id,))
        description_id = self.cursor.fetchone()

        if description_id:
            self.cursor.execute("UPDATE Descriptions SET description=? WHERE id=?", (description, description_id[0]))
        else:
            self.cursor.execute("INSERT INTO Descriptions(theme_id, description) VALUES (?,?)", (theme_id, description))

        self.commit()

    def get_description(self, theme_id: int) -> str:
        self.cursor.execute("SELECT description FROM Descriptions WHERE theme_id=?", (theme_id,))
        description = self.cursor.fetchone()

        if description is None:
            description = ('', )
            self.cursor.execute("INSERT INTO Descriptions(theme_id, description) VALUES (?, '')", (theme_id,))
            self.commit()
        return description[0]


def format_date_dict(date_dict: dict):
    match date_dict:
        case {'month': None, 'day': None}:
            date_dict['month'] = 'NULL'
            date_dict['day'] = 'NULL'
        case {'day': None}:
            date_dict['day'] = 'NULL'
        case _:
            pass

    return date_dict['year'], date_dict['month'], date_dict['day']


def date_from_formatted(format_date: tuple[str, str, str]):
    date_dict = {'year': None, 'month': None, 'day': None}
    for key, value in zip(date_dict.keys(), format_date):
        if value != 'NULL':
            date_dict[key] = value

    return date_dict
