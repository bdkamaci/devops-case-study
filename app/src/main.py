from flask import Flask, jsonify, request
import os
import logging
from datetime import datetime

app = Flask(__name__)

# Logging Config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "DevOps Case Study Application",
        "environment": os.getenv('APP_ENVIRONMENT', 'development'),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health_check():
    try:
        # Basic Health Check Logic
        return jsonify({
            "status": "healthy",
            "environment": os.getenv('APP_ENVIRONMENT', 'development')
        })
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

@app.route('/config')
def get_config():
    # Simulate Retrieving Config
    return jsonify({
        "database_host": os.getenv('DB_HOST', 'localhost'),
        "app_name": os.getenv('APP_NAME', 'DevOps Case Study')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)