from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mordio30:QWErty@localhost/students"
db = SQLAlchemy(app)

with app.app_context():
    result = db.session.execute(text("SELECT 1"))
    print(result.fetchall())
