from flask import Flask, jsonify
from datetime import datetime
import psycopg2
import os

app = Flask(__name__)

# PostgreSQL connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "postgres-service"),
        database=os.environ.get("DB_NAME", "devopsdb"),
        user=os.environ.get("DB_USER", "devops"),
        password=os.environ.get("DB_PASSWORD", "devops123")
    )
    return conn


@app.route("/health")
def health():
    return jsonify(status="UP"), 200


@app.route("/api/message")
def message():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT NOW();")
    db_time = cur.fetchone()[0]

    cur.close()
    conn.close()

    return jsonify(
        message="Hello from Flask Backend 🚀",
        timestamp=str(datetime.utcnow()),
        database_time=str(db_time)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)