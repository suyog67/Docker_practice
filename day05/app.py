from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('http://api-service:5001/data')
        data = response.json()
        return f'Message from API container: {data["message"]}'
    except:
        return 'Could not connect to API container!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
