from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "userName": self.userName,
            "email": self.email
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(250))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    url = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(30))
    gender = db.Column(db.String(250))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    name = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    url = db.Column(db.String(250))

    def serialize(self):
            return {
                "id": self.id,
                "height": self.height,
            }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(250))
    maufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.String(250))
    length = db.Column(db.Float)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(250))
    films = db.Column(db.String(250))
    pilots = db.Column(db.String(250))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    name = db.Column(db.String(250))
    url = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    favorite_char = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship(Character)
    favorite_planet = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship(Planet)
    favorite_vehicle = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicle = db.relationship(Vehicle)

    def serialize(self):
        return {
            "id": self.id,
            "favorite_user": self.favorite_user,
            "favorite_char": self.favorite_char,
            "favorite_planet": self.favorite_planet,
            "favorite_vehicle": self.favorite_vehicle,
            # do not serialize the password, its a security breach
        }

"""     def to_dict(self):
        return {}

    def __repr__(self):
        return '<User %r>' % self.username """

