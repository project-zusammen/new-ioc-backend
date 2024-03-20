from app import app
from app.controllers import student_controller

@app.route("/")
def index():
    return "Success"


@app.route("/student", methods=["POST"])
def student():
    return student_controller.student_register()