#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    
    animal = Animal.query.filter(Animal.id == id).first()

    response_body = f'''
            <h1>ID: {animal.id}</h1>
            <h1>Name: {animal.name}</h1>
            <h1>Species: {animal.species}</h1>

    '''
    zookeeper = animal.zookeeper

    if not zookeeper:
        response_body += '<h1>no zookepeer</h1>'
    else:
        response_body += f'<h1>Zookeeper: {zookeeper.name}'

    enclosure = animal.enclosure
    if not enclosure:
        response_body += '<h1>no enclosure</h1>'
    else:
        response_body += f'<h1>Zookeeper: {enclosure.environment}'




    response = make_response(response_body, 200)

    return response

   

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    return ''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return ''


if __name__ == '__main__':
    app.run(port=5505, debug=True)
