from my_functions import build_experiment, build_person

if __name__ == "__main__":

    supervisorr = "Manuel Hager"
    subject = build_person("Max","Mustermann","male",20)
    experiment = build_experiment("Test","18-03-20225",supervisorr,subject)
    
    print(experiment)
    