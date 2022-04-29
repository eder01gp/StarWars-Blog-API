"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Character, Vehicle, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def people():
    people = Character.query.all()
    people_serial = list(map(lambda e: e.serialize(),people))

    return jsonify(people_serial), 200

@app.route('/people/<int:character_id>', methods=['GET'])
def charac(character_id):
    charac = Character.query.get(character_id)

    return jsonify(charac.serialize()), 200

@app.route('/planets', methods=['GET'])
def planets():
    planets = Planet.query.all()
    planets_serial = list(map(lambda e: e.serialize(),planets))

    return jsonify(planets_serial), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def planet(planet_id):
    planet = Planet.query.get(planet_id)

    return jsonify(planet.serialize()), 200

@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    users_serial = list(map(lambda e: e.serialize(),users))

    return jsonify(users_serial), 200

@app.route('/user/<int:favorite_user>/favorites', methods=['GET'])
def user_favorites(favorite_user):
    user_favorites = Favorite.query.filter(Favorite.favorite_user==favorite_user)
    user_favorites_serial = list(map(lambda e: e.serialize(),user_favorites))

    return jsonify(user_favorites_serial), 200

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['POST'])
def new_fav_planet(user_id,planet_id):
    check = User.query.get(user_id)
    if check == None:
        return jsonify({"Respuesta":"No existe este usuario"}), 200
    else:
        new_fav_planet = Favorite.query.filter(Favorite.favorite_user==user_id,Favorite.favorite_planet==planet_id)
        if new_fav_planet != None:
            return jsonify({"Respuesta":"Este favorito ya existe"}), 200
        else:
            new_fav_planet = Favorite(favorite_user=user_id,favorite_planet=planet_id)
            db.session.add(new_fav_planet)
            db.session.commit()
            return jsonify({"Usuario":new_fav_planet.favorite_user, "Ha añadido su planeta favorito":new_fav_planet.favorite_planet}), 200
        

@app.route('/user/<int:user_id>/favorite/person/<int:char_id>', methods=['POST'])
def new_fav_char(user_id,char_id):
    check = User.query.get(user_id)
    if check == None:
        return jsonify({"Respuesta":"No existe este usuario"}), 200
    else:
        new_fav_char = Favorite.query.filter(Favorite.favorite_user==user_id,Favorite.favorite_char==char_id)
        if new_fav_char != None:
            return jsonify({"Respuesta":"Este favorito ya existe"}), 200
        else:
            new_fav_char = Favorite(favorite_user=user_id,favorite_char=char_id)
            db.session.add(new_fav_char)
            db.session.commit()
            return jsonify({"Usuario":new_fav_char.favorite_user, "Ha añadido su personaje favorito":new_fav_char.favorite_char}), 200

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['DELETE'])
def del_fav_planet(user_id,planet_id):
    del_fav_planet = Favorite.query.filter(Favorite.favorite_user==user_id,Favorite.favorite_planet==planet_id).first()
    if del_fav_planet == None:
        return jsonify({"Respuesta":"No existe este favorito"}), 200
    else:
        db.session.delete(del_fav_planet)
        db.session.commit()
        return jsonify({"Usuario":del_fav_planet.favorite_user, "Ha borrado su planeta favorito":del_fav_planet.favorite_planet}), 200

@app.route('/user/<int:user_id>/favorite/person/<int:char_id>', methods=['DELETE'])
def del_fav_char(user_id,char_id):
    del_fav_char = Favorite.query.filter(Favorite.favorite_user==user_id,Favorite.favorite_char==char_id).first()
    if del_fav_char == None:
        return jsonify({"Respuesta":"No existe este favorito"}), 200
    else:    
        db.session.delete(del_fav_char)
        db.session.commit()
        return jsonify({"Usuario":del_fav_char.favorite_user, "Ha borrado su personaje favorito":del_fav_char.favorite_char}), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
