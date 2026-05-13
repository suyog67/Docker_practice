from flask import Flask, jsonify, request
import psycopg2
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

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

@app.route('/health')
def health():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "healthy"}), 200
    except:
        return jsonify({"status": "unhealthy"}), 500

@app.route('/tasks', methods=['GET'])
def get_tasks():
    logger.info('Getting all tasks')
    conn = get_db()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, task TEXT);')
    cur.execute('SELECT * FROM tasks;')
    tasks = cur.fetchall()
    conn.commit()
    conn.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    logger.info(f'Adding task: {task}')
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (task) VALUES (%s)', (task,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Task '{task}' added!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
