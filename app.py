from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpassword",
            database="testdb"
        )

        if db.is_connected():
            db.close()
            return "Flask connected successfully to MySQL!"

    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)