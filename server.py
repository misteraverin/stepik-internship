import requests
from werkzeug.contrib.cache import SimpleCache
from flask import Flask, request, jsonify
from stepik_model import stepik_api


cache = SimpleCache()
app = Flask(__name__)
stepik = stepik_api()

@app.route('/api/steps/lesson=<int:lesson_id>')
def lessons(lesson_id):
    
    try:
        lesson_id = int(lesson_id)
        ids = [12, 13]
        #response = requests.get(url, params={'ids[]': ids})
        return jsonify({lesson_id: ids})
    except Exception as e:
        response = jsonify(message="Invalid Lesson ID: "+lesson_id)
        response.status_code = 404
        return jsonify(response)
    

def main():
    app.run(threaded=True)

if __name__ == '__main__':
    main()