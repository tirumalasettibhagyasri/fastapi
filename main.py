from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student Details Management API")
students_db = {
    1:{"name":"BhagyaSri","age":21,"course":"Data Analytics"}
    2:{"name":"Harika","age":21,"course":"Data Analytics"}
    3:{"name":"Lakshmi Durga","age":22,"course":"Data Analytics"}
    4:{"name":"Srija","age":21,"course":"Data Science"}
}

#2.Data Validation Model

class Student(BaseModel):
    name: str
    age: int
    course: str

#READ (GET) - View All or Filter by Course
@app.get("/students/")
def get_students(course: str = None):
    if course:
        filtered = {
            s_id: s
            for s_id, s in students_db.items()
            if s["course"].lower() == course.lower()
        }
        return filtered

    return students_db
# READ SINGLE STUDENT BY ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students_db:
        return {"error": "Student not found"}
    return students_db[student_id]
    





