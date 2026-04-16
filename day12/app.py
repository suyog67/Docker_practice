from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def read_secret(secret_name):
    try:
        with open(f'/run/secrets/{secret_name}', 'r') as f:
            return f.read().strip()
    except:
        return os.environ.get(secret_name.upper())

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=read_secret('db_user'),
        password=read_secret('db_password')
    )

@app.route('/')
def home():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "connected", "message": "Secrets are working!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
