from database import Database
import random as rand


months_1 = {
    1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
    7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'
}
months_2 = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
    7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
}


class Task:
    def __init__(self, question: str | dict, umn: bool = True):  # umn - use months names
        self.is_date_task = False
        self.is_event_task = False
        self.umn = umn
        self.question: str | dict = question
        self.answers: dict[str:bool] = dict()

    def __call__(self, answer: str | dict = '', is_correct: bool = False, *args, get_answer: bool = False):
        if not any((self.is_date_task, self.is_event_task)):
            if isinstance(answer, dict):
                if self.umn:
                    match answer:
                        case {'year': year, 'month': None, 'day': None}:
                            answer = year
                        case {'year': year, 'month': month, 'day': None}:
                            answer = f'{months_1[int(month)]} {year}'
                        case {'year': year, 'month': month, 'day': day}:
                            answer = f'{int(day)} {months_2[int(month)]} {year}'
                else:
                    match answer:
                        case {'year': year, 'month': None, 'day': None}:
                            answer = year
                        case {'year': year, 'month': month, 'day': None}:
                            answer = f'{month:>02}.{year:>04}'
                        case {'year': year, 'month': month, 'day': day}:
                            answer = f'{day:>02}.{month:>02}.{year:>04}'
            self.answers.update({answer: is_correct})
        else:
            if get_answer:
                return [ans for ans in self.answers.keys() if self.answers[ans]][0]

            queue = [ans for ans in self.answers.keys()]
            queue.sort(key=lambda x: rand.randint(0, 10**6))
            return {'question': self.question, 'answers': queue}

    def complete(self):
        if isinstance(self.question, dict):
            self.is_date_task = True
            if self.umn:
                match self.question:
                    case {'year': year, 'month': None, 'day': None}:
                        self.question = year
                    case {'year': year, 'month': month, 'day': None}:
                        self.question = f'{months_1[int(month)]} {year}'
                    case {'year': year, 'month': month, 'day': day}:
                        self.question = f'{int(day)} {months_2[int(month)]} {year}'
            else:
                match self.question:
                    case {'year': year, 'month': None, 'day': None}:
                        self.question = year
                    case {'year': year, 'month': month, 'day': None}:
                        self.question = f'{month:>02}.{year:>04}'
                    case {'year': year, 'month': month, 'day': day}:
                        self.question = f'{day:>02}.{month:>02}.{year:>04}'
        else:
            self.is_event_task = True


class Combinator:
    def __init__(self, db: Database, theme_id: int):
        self.db: Database = db
        self.__is_date_task = False
        self.__is_event_task = False

        self.__theme_id = theme_id
        self.__theme: list = []

        self.__question: str | dict | None = None
        self.__answers = []

    def __load_events(self, theme_id: int):
        data = self.db.get_events_by_theme(theme_id)
        for event in data:
            event.pop('id')
        return data

    def __range_date(self):
        date: dict = self.__answers[0]
        key = rand.choice([key for key in date.keys() if date[key]])
        available_shifts = [-3, -2, -1, 1, 2, 3]

        for _ in range(3):
            shift = rand.choice(available_shifts)
            available_shifts.remove(shift)

            n_date = date.copy()

            value = int(n_date[key]) + shift
            if key == 'month' and value > 12:
                value -= 12
            elif key == 'month' and value < 1:
                value += 12
            if key == 'day' and value > 30:
                value -= 30
            elif key == 'day' and value < 1:
                value += 30

            n_date[key] = f"{value:0>2}"
            self.__answers.append(n_date)

        return 1

    def __mix_date(self):
        dates = self.db.get_random_dates(self.__answers[0])

        if dates:
            for date in dates:
                self.__answers.append(date)
            return 1
        return 0

    def __mix_event(self):
        for event in self.db.get_random_events(self.__answers[0]):
            self.__answers.append(event)

    def __mix_date_by_theme(self):
        if len(self.__theme) >= 4:
            theme_dates = [event['date'].copy() for event in self.__theme]
            theme_dates.remove(self.__answers[0])

            for _ in range(3):
                rand_date = rand.choice(theme_dates)
                theme_dates.remove(rand_date)
                self.__answers.append(rand_date)

            return 1
        return 0

    def __mix_event_by_theme(self):
        if len(self.__theme) >= 4:
            theme_events = [event['event'] for event in self.__theme]
            theme_events.remove(self.__answers[0])

            for _ in range(3):
                rand_event = rand.choice(theme_events)
                theme_events.remove(rand_event)
                self.__answers.append(rand_event)

            return 1
        return 0

    def __get_strategies(self):
        dates_starts = {
            'range_dates': self.__range_date,
            'mix_dates': self.__mix_date_by_theme,
            'mix_external_dates': self.__mix_date
        }
        events_starts = {
            'mix_external_events': self.__mix_event
        }

        settings = self.db.get_settings()
        strats = []
        if self.__is_event_task:
            for name, f in dates_starts.items():
                if settings[name]:
                    strats.append(f)
        else:
            for name, f in events_starts.items():
                if settings[name]:
                    strats.append(f)
            strats.append(self.__mix_event_by_theme)

        return strats

    def generate_task(self):
        if rand.randint(0, 1):
            self.__is_date_task = True
            self.__is_event_task = False
        else:
            self.__is_event_task = True
            self.__is_date_task = False

        self.__theme = self.__load_events(self.__theme_id)

        main_event = rand.choice(self.__theme)
        self.__question = main_event['event'] if self.__is_event_task else main_event['date']
        self.__answers = [main_event['event'] if self.__is_date_task else main_event['date']]

        strategies = self.__get_strategies()

        strategy = rand.choice(strategies)
        while strategy() == 0:
            strategies.remove(strategy)
            strategy = rand.choice(strategies)

        umn = bool(self.db.get_settings()['use_months_names'])
        task = Task(self.__question, umn=umn)
        for i, answer in enumerate(self.__answers):
            task(answer=answer, is_correct=i == 0)
        task.complete()
        return task
    