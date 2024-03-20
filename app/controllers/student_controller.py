from app.models.student import Student
from app import response, app, db
from flask import request, jsonify
import uuid

def format_student(student):
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email
    }

def student_register():
    try:
        id = str(uuid.uuid4())
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        student = Student(
            id=id,
            name=name,
            email=email
        )
        student.setPassword(password)
        db.session.add(student)
        db.session.commit()

        return response.success("", "Student register success")
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500