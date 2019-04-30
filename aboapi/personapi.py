from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
import os
import logging

app = Flask(__name__)
CORS(app)
logging.getLogger('flask_cors').level = logging.DEBUG
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'person.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost:5433/abodb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:15333/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@abodb.abo.svc.cluster.local:5432/postgres'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nachname = db.Column(db.String(80), unique=False, nullable=False)
    vorname = db.Column(db.String(80), unique=False, nullable=False)
    geburtstag = db.Column(db.String(20), unique=False, nullable=False)
    blutgruppe = db.Column(db.String(10), unique=False, nullable=True)

    def __init__(self, nachname, vorname, geburtstag, blutgruppe):
        self.nachname = nachname
        self.vorname = vorname
        self.geburtstag = geburtstag
        self.blutgruppe = blutgruppe


class PersonSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','nachname', 'vorname','geburtstag','blutgruppe')


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

@app.route("/api/v1/person/", methods=["POST"])
def add_person():
    nachname = request.json['nachname']
    vorname = request.json['vorname']
    geburtstag = request.json['geburtstag']
    blutgruppe = request.json['blutgruppe']
    
    new_person = Person(nachname, vorname, geburtstag, blutgruppe)

    db.session.add(new_person)
    db.session.commit()

    return person_schema.jsonify(new_person)


@app.route("/api/v1/person/", methods=["GET"])
def get_person():
    all_persons = Person.query.all()
    result = persons_schema.dump(all_persons)
    return jsonify(result.data)


@app.route("/api/v1/person/<id>", methods=["GET"])
def person_detail(id):
    person = Person.query.get(id)
    return person_schema.jsonify(person)


@app.route("/api/v1/person/<id>", methods=["PUT"])
def person_update(id):
    person = Person.query.get(id)
    nachname = request.json['nachname']
    vorname = request.json['vorname']
    geburtstag = request.json['geburtstag']
    blutgruppe = request.json['blutgruppe']

    person.nachname = nachname
    person.vorname = vorname
    person.geburtstag = geburtstag
    person.blutgruppe = blutgruppe

    db.session.commit()
    return person_schema.jsonify(person),200


@app.route("/api/v1/person/<id>", methods=["DELETE"])
def person_delete(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()

    return person_schema.jsonify(person)


if __name__ == '__main__':
    app.run(debug=True)