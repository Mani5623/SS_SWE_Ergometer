from my_classes import Subject, Supervisor, Experiment
from datetime import date

if __name__ == "__main__":
    # Supervisor-Daten mit Geburtsdatum
    supervisor = Supervisor("Jakob", "Haas", date(2005, 7, 24))

    # Versuchsperson-Daten mit Geburtsdatum
    subject = Subject("Hanne", "Müller", "female", date(1969, 2, 20))
    subject.estimate_max_hr()

    # Experiment-Daten
    experiment = Experiment("Herzfrequenz-Analyse", "2025-04-10")
    experiment.add_supervisor(supervisor)
    experiment.add_subject(subject)

    # Ausgabe des Experiments
    print(experiment)


#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

# GET all persons
@app.route('/person/', methods=['GET'])
def get_persons():
    with open('data.json', 'r') as f:
        data = f.read()
        return data


# POST (create a new person)
@app.route('/person/', methods=['POST'])
def create_person():
    record = json.loads(request.data)
    with open('data.json', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('data.json', 'w') as f:
        f.write(json.dumps(records, indent=2))
    response = jsonify(record)
    response.status_code = 201
    response.headers['Location'] = f"/person/{record['id']}"
    return response

# GET a person by id
@app.route('/person/<id>', methods=['GET'])
def get_person(id):

    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['id'] == id:
                return jsonify(record)
        return jsonify({'error': 'data not found'})
    
# PUT (update a person)
@app.route('/person/<id>', methods=['PUT'])

def update_person(id):
    record = json.loads(request.data)
    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for i in range(len(records)):
            if records[i]['id'] == id:
                records[i] = record
                with open('data.json', 'w') as f:
                    f.write(json.dumps(records, indent=2))
                return jsonify(record)
        return jsonify({'error': 'data not found'})

# DELETE a person
@app.route('/person/<id>', methods=['DELETE'])

def delete_person(id):

    with open('data.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for i in range(len(records)):
            if records[i]['id'] == id:
                record = records.pop(i)
                with open('data.json', 'w') as f:
                    f.write(json.dumps(records, indent=2))
                record["deleted"] = "True"
                return jsonify(record)
        return jsonify({'error': 'data not found'})


# GET all persons
@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

app.run(debug=True)