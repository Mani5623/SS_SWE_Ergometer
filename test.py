import json
from my_functions import Person, Subject, Experiment

if __name__ == "__main__":
    # Personen erzeugen
    supervisor = Person("Jakob", "Haas", "male", 19)
    supervisor.put()

    subject = Subject("Hanne", "Müller", "female", 56, email="hanne@example.com")
    subject.put()
    subject.update_email()

    # Experiment erzeugen
    experiment = Experiment("Herzfrequenz-Analyse", "2025-04-10", supervisor, subject)

    #Experiment speichern
    experiment.save_to_json_file("experiment.json")

    # JSON-Output
    print(json.dumps(experiment.to_dict(), indent=4, ensure_ascii=False))
    print("Experiment wurde gespeichert in experiment.json.")


