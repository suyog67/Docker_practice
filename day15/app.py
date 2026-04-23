from flask import Flask, jsonify
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    logger.info('Home endpoint was called')
    return jsonify({"message": "Logging demo!"})

@app.route('/error')
def error():
    logger.error('Something went wrong!')
    return jsonify({"message": "Error logged!"}), 500

@app.route('/warning')
def warning():
    logger.warning('This is a warning!')
    return jsonify({"message": "Warning logged!"})

if __name__ == '__main__':
    logger.info('Starting Flask application')
    app.run(host='0.0.0.0', port=5000)
