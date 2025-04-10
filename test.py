from my_classes import Subject, Supervisor, Experiment
from datetime import datetime

if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("Manuel", "Hager")
    
    # Geburtsdatum als datetime-Objekt anstelle des Alters
    birthdate = datetime(2004, 6, 3) 
    subject = Subject("Max", "Mustermann", "male", birthdate)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)
