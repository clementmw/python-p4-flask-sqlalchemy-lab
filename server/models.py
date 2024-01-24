from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday  = db.Column(db.Date)
    
    # relationship to animal
    animals = db.relationship('Animal', backref = 'zookeeper')

    def __repr__(self):
        return f"name {self.name}"\
        f"birthday {self.birthday}"

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean, default = False)

    # relationship to animal
    animals = db.relationship('Animal', backref = 'enclosure')

    def __repr__(self):
        return f"environment{self.environment}"

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    # relationship to zookeeper
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    # relationship to enclosure
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    
    def __repr__(self):
        return f"name {self.name}"\
        f"species {self.species}"

  
