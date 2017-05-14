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
        if lesson_id < 0:
            raise ValueError
        date = stepik.get_lesson_date(lesson_id)
    except Exception, ValueError as e:
        response = jsonify(status="Error", message="Invalid Lesson ID: "+lesson_id)
        response.status_code = 404
        return response

    cached = simple_cache.get(str(lesson_id))

    if not cached or cached[0] != date:
        steps = stepik.get_steps_id(lesson_id)
        simple_cache.set(str(lesson_id), (date, steps))
    else:
        steps = cached[1]
    return jsonify({"ids": steps})

def main():
    app.run(threaded=True)

if __name__ == '__main__':
    main()