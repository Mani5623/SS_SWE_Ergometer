class Subject():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = None

    def estimate_max_hr(self):
        """A function that estimates the maximum heart rate of a subject"""
        if self.sex == "male":
            self.max_hr = 220 - self.age
        elif self.sex == "female":
            self.max_hr = 226 - self.age
        return self.max_hr

class Supervisor():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Experiment():
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
        return f"Experiment: {self.name}, Date: {self.date}, Subject: {self.subject.first_name} {self.subject.last_name}, Supervisor: {self.supervisor.first_name} {self.supervisor.last_name}"
