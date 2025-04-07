class Subject:
    def __init__(self, first_name: str, last_name: str, sex: str, age: int):
        """Initialisiert ein Subject-Objekt mit persönlichen Daten."""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = None  # Wird später durch estimate_max_hr() gesetzt

    def estimate_max_hr(self):
        """Berechnet die maximale Herzfrequenz basierend auf Geschlecht und Alter."""
        if self.sex.lower() == "male":
            self.max_hr = 223 - 0.9 * self.age
        elif self.sex.lower() == "female":
            self.max_hr = 226 - 1.0 * self.age
        else:
            self.max_hr = input("Enter maximum heart rate: ")

        self.max_hr = int(self.max_hr)

    def __repr__(self):
        return f"Subject({self.first_name} {self.last_name}, {self.sex}, {self.age} Jahre, max HR: {self.max_hr})"


class Supervisor:
    def __init__(self, first_name: str, last_name: str):
        """Initialisiert ein Supervisor-Objekt."""
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Supervisor({self.first_name} {self.last_name})"


class Experiment:
    def __init__(self, name: str, date: str):
        """Initialisiert ein Experiment-Objekt."""
        self.name = name
        self.date = date
        self.supervisor = None
        self.subject = None

    def add_subject(self, subject: Subject):
        """Fügt eine Versuchsperson zum Experiment hinzu."""
        self.subject = subject

    def add_supervisor(self, supervisor: Supervisor):
        """Fügt eine Versuchsleitung zum Experiment hinzu."""
        self.supervisor = supervisor

    def __repr__(self):
        return f"Experiment({self.name}, {self.date}, Supervisor: {self.supervisor}, Subject: {self.subject})"
