from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )

@app.route('/')
def home():
    return jsonify({"status": "healthy", "message": "App is running!"})

@app.route('/health')
def health():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except:
        return jsonify({"status": "unhealthy", "database": "disconnected"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
