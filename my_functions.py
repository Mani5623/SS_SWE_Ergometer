import requests

class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def put(self):
        url = "http://localhost:5000/api/person"
        data = {"first_name": self.first_name}
        response = requests.post(url, json=data)
        print(f"PUT Person: {response.status_code} – {response.text}")


class Subject(Person):
    def __init__(self, first_name, last_name, gender, age, email=""):
        super().__init__(first_name, last_name, gender, age)
        self.email = email

    def update_email(self):
        url = "http://localhost:5000/api/person/email"
        data = {"first_name": self.first_name, "email": self.email}
        response = requests.post(url, json=data)
        print(f"Update Email: {response.status_code} – {response.text}")


def build_person(first_name, last_name, gender, age, email=None):
    if email:
        return Subject(first_name, last_name, gender, age, email)
    else:
        return Person(first_name, last_name, gender, age)


def build_experiment(title, date, supervisor, subject):
    return {
        "title": title,
        "date": date,
        "supervisor": vars(supervisor),
        "subject": vars(subject),
    }
