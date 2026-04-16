from flask import Flask, jsonify, request
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
    return jsonify({"message": "Todo API is running!"})

@app.route('/todos', methods=['GET'])
def get_todos():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, task TEXT);')
    cur.execute('SELECT * FROM todos;')
    todos = cur.fetchall()
    conn.commit()
    conn.close()
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    task = request.json.get('task')
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO todos (task) VALUES (%s)', (task,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Todo '{task}' added!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
