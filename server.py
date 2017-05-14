import requests
from werkzeug.contrib.cache import SimpleCache
from flask import Flask, request, jsonify
from stepik_api import stepik_api


cache = SimpleCache()
app = Flask(__name__)
stepik = stepik_api()

@app.route('/api/steps/lesson=<int:lesson_id>')
def lessons(lesson_id):
    
    try:
        lesson_id = int(lesson_id)
    except Exception as e:
        response = jsonify(status="Error", message="Invalid Lesson ID: "+lesson_id)
        response.status_code = 404
        return response
    
    try:
        lesson_id = int(lesson_id)
    except ValueError:
        response = jsonify(status="Error", message="Lesson ID: "+lesson_id + " is less than zero.")
        response.status_code = 404
        return response
    return jsonify({"ids": stepik.get_steps_id(lesson_id)})

def main():
    app.run(threaded=True)

if __name__ == '__main__':
    main()