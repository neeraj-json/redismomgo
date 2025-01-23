#Installing flask, pymongo, flask_pymongo

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://neeraj:Support%4012345@travelmemory.6rrh4zg.mongodb.net/flaskdummydata"
mongo = PyMongo(app)


@app.route('/hello', methods=['GET'])
def hello():
    return "hello world"

@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify({"err": "Missing name or age"}), 400
    
    mongo.db.employee.insert_one({"name":name, "age": age})
    return jsonify({"msg": "Data added succesfully"}), 201

@app.route('/get_direct/<name>', methods=['GET'])
def get_data_directly(name):
    data = mongo.db.employee.find_one({"name": name})
    if data:
        return jsonify({"msg":"User found"}), 200
    return jsonify({"msg":"data not available"}), 404

if __name__ == "__main__":
    app.run(debug=True)