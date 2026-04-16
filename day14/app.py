from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Resource management demo!",
        "memory_limit": os.environ.get('MEMORY_LIMIT', 'not set'),
        "cpu_limit": os.environ.get('CPU_LIMIT', 'not set')
    })

@app.route('/stress')
def stress():
    # simulates CPU stress
    result = 0
    for i in range(10000000):
        result += i
    return jsonify({"result": result, "message": "CPU stress test done!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
