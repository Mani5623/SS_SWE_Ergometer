from my_functions import build_experiment, build_person

if __name__ == "__main__":
    # Supervisor-Daten
    supervisor = build_person("Jakob", "Haas", "male", 19)

    # Versuchsperson-Daten
    subject = build_person("Hanne", "Müller", "female", 56)

    # Experiment-Daten
    experiment = build_experiment("Herzfrequenz-Analyse", "2025-03-24", supervisor, subject)

    # Ausgabe des Experiment-Dictionarys
    print(experiment)