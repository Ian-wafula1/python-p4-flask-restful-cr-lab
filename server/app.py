#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    
    def get(self):
        plants = [p.to_dict() for p in Plant.query.all()]
        return make_response(plants, 200, {'Content-Type': 'application/json'})
    
    def post(self):
        data = request.get_json()
        plant = Plant(
            name=data['name'],
            image=data['image'],
            price=data['price'],
        )
        db.session.add(plant)
        db.session.commit()
        return make_response(plant.to_dict(), 200, {'Content-Type': 'application/json'})

class PlantByID(Resource):
    
    def get(self, id):
        plant = Plant.query.filter_by(id=id).first()
        return make_response(plant.to_dict(), 200, {'Content-Type': 'application/json'})

api.add_resource(Plants, '/plants')
api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
