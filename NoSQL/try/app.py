from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

# Configuration
app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")  # Adresse de MongoDB

# Accès à la base de données et à la collection
db = client['taskdb']
task_collection = db['tasks']

# Routes

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = list(task_collection.find())
    for task in tasks:
        task['_id'] = str(task['_id'])
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {'title': data['title'], 'done': False}
    result = task_collection.insert_one(task)
    task['_id'] = str(result.inserted_id)
    return jsonify(task), 201

@app.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        task = task_collection.find_one({'_id': ObjectId(task_id)})
        if not task:
            return jsonify({'error': 'Task not found'}), 404

        data = request.get_json()
        task_collection.update_one({'_id': ObjectId(task_id)}, {'$set': {
            'title': data.get('title', task['title']),
            'done': data.get('done', task['done'])
        }})
        task = task_collection.find_one({'_id': ObjectId(task_id)})
        task['_id'] = str(task['_id'])
        return jsonify(task)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        result = task_collection.delete_one({'_id': ObjectId(task_id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Task not found'}), 404
        return jsonify({'message': 'Task deleted'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
