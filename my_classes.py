from datetime import date

class Person:
    def __init__(self, first_name: str, last_name: str, birthdate: date):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = birthdate

    def _calculate_age(self) -> int:
        today = date.today()
        age = today.year - self.__birthdate.year - (
            (today.month, today.day) < (self.__birthdate.month, self.__birthdate.day)
        )
        return age

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(Person):
    def __init__(self, first_name: str, last_name: str, sex: str, birthdate: date):
        super().__init__(first_name, last_name, birthdate)
        self.sex = sex
        self.max_hr = None

    def estimate_max_hr(self):
        age = self._calculate_age()
        if self.sex.lower() == "male":
            self.max_hr = int(223 - 0.9 * age)
        elif self.sex.lower() == "female":
            self.max_hr = int(226 - 1.0 * age)
        else:
            self.max_hr = int(input("Enter maximum heart rate: "))

    def __repr__(self):
        return f"Subject({super().__repr__()}, {self.sex}, max HR: {self.max_hr})"


class Supervisor(Person):
    def __init__(self, first_name: str, last_name: str, birthdate: date):
        super().__init__(first_name, last_name, birthdate)

    def __repr__(self):
        return f"Supervisor({super().__repr__()})"


class Experiment:
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date
        self.supervisor = None
        self.subject = None

    def add_subject(self, subject: Subject):
        self.subject = subject

    def add_supervisor(self, supervisor: Supervisor):
        self.supervisor = supervisor

    def __repr__(self):
        return (f"Experiment({self.name}, {self.date}, "
                f"Supervisor: {self.supervisor}, Subject: {self.subject})")
