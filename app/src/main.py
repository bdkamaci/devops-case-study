from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to DevOps Case Study Application",
        "environment": os.getenv('APP_ENVIRONMENT', 'development')
    })

@app.route('/health')
def health_check():
    try:
        # Attempt to connect to the database
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'myapp'),
            user=os.getenv('DB_USER', 'myuser'),
            password=os.getenv('DB_PASSWORD', 'mypassword')
        )
        conn.close()
        return jsonify({"status": "healthy"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)