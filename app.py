from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mordio30:password@localhost/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Students(db.Model):  # referencing our table as a Model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(2))


@app.route('/old_students/', methods=['GET'])
def old_students():
    query = text("SELECT * FROM students WHERE age >= 21")
    result = db.session.execute(query)
    json_students = [{'id': row.id, 'first_name': row.first_name, 'last_name': row.last_name, 'age': row.age, 'grade': row.grade} for row in result.mappings()]
    return jsonify(json_students)

@app.route('/advance_students/', methods=['GET'])
def advance_students():
    query = text("SELECT * FROM students WHERE age <= 20 AND grade = 'A'")
    result = db.session.execute(query)
    json_students = [{'id': row.id, 'first_name': row.first_name, 'last_name': row.last_name, 'age': row.age, 'grade': row.grade} for row in result.mappings()]
    return jsonify(json_students)


@app.route('/student_names/', methods=['GET'])
def student_names():
    query = text("SELECT first_name, last_name FROM students")
    result = db.session.execute(query)
    json_students = [{'first_name': row.first_name, 'last_name': row.last_name} for row in result.mappings()]
    return jsonify(json_students)


@app.route('/student_ages/', methods=['GET'])
def student_ages():
    query = text("SELECT first_name || ' ' || last_name AS student_name, age FROM students")
    result = db.session.execute(query)
    json_students = [{'student_name': row.student_name, 'age': row.age} for row in result.mappings()]
    return jsonify(json_students)


@app.route('/students/', methods=['GET'])
def all_students():
    query = text("SELECT * FROM students")
    result = db.session.execute(query)
    json_students = [{'id': row.id, 'first_name': row.first_name, 'last_name': row.last_name, 'age': row.age, 'grade': row.grade} for row in result.mappings()]
    return jsonify(json_students)


# if __name__ == '__main__':
app.run(debug=True, port=8000)
