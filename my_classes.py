from datetime import datetime

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__birthdate = birthdate  # Privates Attribut
        self.max_hr = None
        self.age = self._calculate_age()

    def _calculate_age(self):
        """Berechnet das Alter basierend auf dem Geburtsdatum"""
        today = datetime.now().date()
        born = self.__birthdate.date() if isinstance(self.__birthdate, datetime) else self.__birthdate
        
        age = today.year - born.year
        
        # Korrektur, falls der Geburtstag in diesem Jahr noch nicht erreicht wurde
        if today < datetime(today.year, born.month, born.day).date():
            age -= 1
            
        return age

    def estimate_max_hr(self):
        """Berechnet die maximale Herzfrequenz basierend auf dem Alter"""
        if self.sex == "male":
            self.max_hr = 223 - 0.9 * self.age
        elif self.sex == "female":
            self.max_hr = 226 - 1.0 * self.age
        return self.max_hr

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subject = None
        self.supervisor = None

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor
        
    def __str__(self):
        subject_info = f"Subject: {self.subject.first_name} {self.subject.last_name}, Sex: {self.subject.sex}, Age: {self.subject.age}"
        return f"Experiment: {self.name}, Date: {self.date}, {subject_info}, Supervisor: {self.supervisor.first_name} {self.supervisor.last_name}"
