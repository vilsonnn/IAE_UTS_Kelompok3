from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({
        'id': user_id,
        'name': f'Mahasiswa {user_id}',
        'role': 'student'
    })

if __name__ == '__main__':
    app.run(port=5001)


import requests

@app.route('/users/<int:user_id>/courses')
def get_user_courses(user_id):
    response = requests.get(f'http://localhost:5002/courses/teacher/{user_id}')
    courses = response.json()
    return jsonify({
        'user_id': user_id,
        'courses': courses
    })
