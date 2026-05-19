from flask import Flask, jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, db=0)

@app.route('/api/visits')
def visits():
    count = redis.incr('page_views')
    return jsonify(message='Hola desde el backend', visits=count)

@app.route('/api/health')
def health():
    return jsonify(status='ok')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
