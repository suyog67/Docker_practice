from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask behind Nginx!"})

@app.route('/api/status')
def status():
    return jsonify({"status": "running", "server": "nginx + flask"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
