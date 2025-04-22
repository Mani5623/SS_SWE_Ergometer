import requests
import json

class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def put(self):
        url = "http://127.0.0.1:5000/api/person"
        data = {"first_name": self.first_name}
        requests.post(url, json=data)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "age": self.age
        }


class Subject(Person):
    def __init__(self, first_name, last_name, gender, age, email=""):
        super().__init__(first_name, last_name, gender, age)
        self.email = email

    def update_email(self):
        url = "http://127.0.0.1:5000/api/person/email"
        data = {"first_name": self.first_name, "email": self.email}
        requests.post(url, json=data)

    def to_dict(self):
        base = super().to_dict()
        base["email"] = self.email
        return base


class Experiment:
    def __init__(self, title, date, supervisor, subject):
        self.title = title
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "supervisor": self.supervisor.to_dict(),
            "subject": self.subject.to_dict()
        }

    def save_to_json_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)
