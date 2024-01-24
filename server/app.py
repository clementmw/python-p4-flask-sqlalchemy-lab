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
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    response_body = f'''
            <h1>ID: {zookeeper.id}</h1>
            <h1> Name: {zookeeper.name}</h1>
            <h1> Birthday: {zookeeper.birthday}

    '''
    animals = zookeeper.animals
    
    if not animals:
        response_body += '<h1>no animals</h1>'
    else:
        for animal in animals:
            response_body += f'<h1>Animal: {animal.name}'

    response = make_response(response_body, 200)
    return response


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    response_body = f'''
            <h1>ID: {enclosure.id} </h1>
            <h1>Environment {enclosure.environment} </h1>
            <h1> Open to Visitors {enclosure.open_to_visitors}</h1>

    ''' 
    enclosed = enclosure.animals
    if not enclosed:
        response_body += f"<h1>no animal found</h1>"
    else:
        for animal in enclosed:
            response_body += f'<h1>Animal: {animal.name}</h1>'

    response = make_response(response_body, 200)
    return response
    


if __name__ == '__main__':
    app.run(port=5505, debug=True)
