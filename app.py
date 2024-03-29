import os
import psycopg2
from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request

CREATE_STUDENTS_TABLE = (
    "CREATE TABLE IF NOT EXISTS student (id SERIAL PRIMARY KEY, name TEXT, rollno INTEGER);"
)
INSERT_STUDENT_RETURN_ID = "INSERT INTO student (name, rollno) VALUES (%s,%s) RETURNING id;"
GET_STUDENT_NAME = """SELECT name FROM student WHERE id = (%s)"""
GET_ALL_STUDENT_NAME = """SELECT * FROM "public"."student" LIMIT 100"""
UPDATE_STUDENT_NAME = """UPDATE student SET name = (%s) WHERE id = (%s)"""
DELETE_STUDENT_NAME = """DELETE FROM student WHERE id = (%s)"""

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


@app.post("/student/create")
def create_student():
    data = request.get_json()
    name = data["name"]
    rollno = data["rollno"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_STUDENTS_TABLE)
            cursor.execute(INSERT_STUDENT_RETURN_ID, (name,rollno,))
            student_id = cursor.fetchone()[0]
    return {"id": student_id, "message": f"{name} created."}, 201


@app.get("/student/get/<int:student_id>")
def get_student(student_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_STUDENT_NAME, (student_id,))
            name = cursor.fetchone()[0]
    return {"name ": name, }, 201


@app.get("/student/getall")
def get_student_all():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ALL_STUDENT_NAME)
            name = cursor.fetchone()[0]
    return {"name ": name, }, 201


@app.post("/student/update/<int:student_id>")
def update_student(student_id):
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(UPDATE_STUDENT_NAME, (name, student_id))
    return {"id": student_id, "message": f"{name} created."}, 201


@app.delete("/student/delete/<int:student_id>")
def delete_student(student_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_STUDENT_NAME, (student_id,))
            # name = cursor.fetchone()[0]
    return {"Deleted Id ": student_id, }, 201
