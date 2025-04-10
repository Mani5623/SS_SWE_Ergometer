from my_classes import Subject, Supervisor, Experiment
from datetime import date

if __name__ == "__main__":
    # Supervisor mit Geburtsdatum
    supervisor = Supervisor("Jakob", "Haas", date(2005, 7, 24))

    # Versuchsperson mit Geburtsdatum
    subject = Subject("Hanne", "Müller", "female", date(1969, 2, 20))
    subject.estimate_max_hr()

    # Experiment anlegen
    experiment = Experiment("Herzfrequenz-Analyse", "2025-04-10")
    experiment.add_supervisor(supervisor)
    experiment.add_subject(subject)

    print(experiment)
