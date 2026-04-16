from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    name = os.environ.get('APP_NAME', 'World')
    env = os.environ.get('APP_ENV', 'development')
    return f'Hello from {name}! Running in {env} mode.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

