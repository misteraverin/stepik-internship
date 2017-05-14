import requests
from werkzeug.contrib.cache import SimpleCache
from flask import Flask, request, jsonify
from stepik_api import stepik_api


simple_cache = SimpleCache()
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

    try:
        date = stepik.get_lesson_date(lesson_id)
    except Eception as e:
        response = jsonify(status="Error", message="Invalid Lesson ID: "+lesson_id)
        response.status_code = 404
        return response

    cached = cache.get(str(lesson_id))

    if not cached or cached[0] != date:
        steps = stepik.get_steps_id(lesson_id)
        cache.set(str(lesson_id), (date, steps))
    else:
        steps = cached[1]
    return jsonify(steps)

def main():
    app.run(threaded=True)

if __name__ == '__main__':
    main()