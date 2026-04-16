from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    count_file = '/app/data/count.txt'
    os.makedirs('/app/data', exist_ok=True)
    
    if not os.path.exists(count_file):
        count = 1
    else:
        with open(count_file, 'r') as f:
            count = int(f.read()) + 1
    
    with open(count_file, 'w') as f:
        f.write(str(count))
    
    return f'This page has been visited {count} times!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

