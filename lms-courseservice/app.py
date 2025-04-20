from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    # Simulasi data course
    course = {
        'id': course_id,
        'title': 'Pemrograman Web',
        'teacher_id': 1
    }

    try:
        # Panggil UserService
        response = requests.get(f'http://127.0.0.1:5001/users/{course["teacher_id"]}')
        response.raise_for_status()  # ini akan raise exception kalau statusnya bukan 200
        teacher = response.json()
    except requests.RequestException as e:
        return jsonify({'error': 'Failed to fetch user', 'detail': str(e)}), 500

    return jsonify({
        'course': course,
        'teacher': teacher
    })

if __name__ == '__main__':
    app.run(port=5002)
