import json
from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from pprint import pprint


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['cardb']
car_collection = db['cars']


@app.get("/")
def index():
    return render_template("index.html")



@app.post('/api/v1/cars')
def save():
    car_dict = request.get_json()
    id = car_collection.insert_one(car_dict).inserted_id
    car_saved = car_collection.find_one({"_id": id}, {"_id": 0, "color": 0})
    return jsonify(car_saved)

@app.get("/api/v1/cars")
def find_all():
    cars = car_collection.find({}, {"_id": 0})
    cars = list(cars)
    return jsonify(cars)


@app.delete("/api/v1/cars/<id>")
def delete_one(id):
    delete = car_collection.delete_one({"_id": id})
    pprint(delete)
    return id



if __name__ == "__main__":
    app.run(debug=False)