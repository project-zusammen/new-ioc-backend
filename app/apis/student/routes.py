from .resources.student_controller import Student
def initialize_routes(api):
    api.add_resource(Student, '/')