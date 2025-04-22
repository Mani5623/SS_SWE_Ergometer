from my_functions import build_person, build_experiment

if __name__ == "__main__":
    # Supervisor anlegen und auf Server speichern
    supervisor = build_person("Jakob", "Haas", "male", 19)
    supervisor.put()

    # Subject mit Email anlegen und speichern
    subject = build_person("Hanne", "Müller", "female", 56, email="hanne.mueller@example.com")
    subject.put()
    subject.update_email()

    # Experiment bauen
    experiment = build_experiment("Herzfrequenz-Analyse", "2025-03-24", supervisor, subject)

    # Experiment-Daten ausgeben
    print(experiment)

