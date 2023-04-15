from fastapi import FastAPI
from user import *
from system import *
from datetime import datetime
from courses import *

# --- Creation Test --- #
teacher = Teacher("teach1", "123456", "teacher1@gmail.com", "tea", "cher", "Male", datetime(2003, 12, 4), "D.Eng",
                  "Bangkok", "Thailand", "KMITL")
admin = Admin("admin", "admin1234", "admin1@gmail.com", "ad", "min", "Male", datetime(2003, 12, 4), "",
              "Bangkok", "Thailand")
student = Student("ffwatcharin", "firstbigdick", "ffwatcharin@gmail.com", "Watcharin", "Humthong", "Male",
                  datetime(2004, 1, 16), "Undergraduated", "Nonthaburi", "Thailand")

course = Courses("SOFT001", "Object Oriented Programming", "Learn writing oop", "teach1", "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")
course2 = Courses("HARD001", "Basic Arduino", "Learn Basic Arduino", "teach1", "Hardware", "All Ages",
                  "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
# --- Build Test --- #
course_system = CourseSystem()

course_system.create_course(course)
course_system.create_course(course2)

course_system.add_user(teacher)
course_system.add_user(student)
course_system.add_user(admin)
print(course_system.get_user_db())

student.set_enrolled_course('enroll', course)  # Student has enrolled SOFT001.

app = FastAPI()

@app.get("/", tags=['root'])
async def root():
    return {"Welcome": "Hello OOP"}


# --- User API --- #
#register
@app.post("/register" , tags=["User API"])
async def register(form_data: dict):
    username = form_data["username"]
    password = form_data["password"]
    email = form_data["email"]
    fname = form_data["fname"]
    lname = form_data["lname"]
    gender = form_data["gender"]
    birth_date = form_data["birth_date"]
    education = form_data["education"]
    province = form_data["province"]
    country = form_data["country"]
    user_type = form_data["user_type"]


    course_system.add_user(User(username=username, password=password, email=email, fname=fname, lname=lname, gender=gender, birth_date=birth_date, education=education, province=province,
                                country=country, user_type=user_type))
    return {
        "messsage": "user created"
    }

#check create users
@app.get("/users", tags=["User API"])
async def read_users():
    return course_system.get_user_db()

@app.get("/login", tags=["User API"])
async def login():
    pass


# --- Course API --- #
@app.get("/courses", tags=["Course API"])
async def courses():
    pass


# --- Enroll API --- #
@app.get("/cart", tags=["Enrollment"])
async def cart():
    return {"Cart": course_system.get_cart()}


@app.post("/addcart", tags=["Enrollment"])
async def add_cart(cart_item: dict) -> dict:
    username = cart_item["username"]
    refcode = cart_item["refcode"]

    print(username)
    print(refcode)

    u = course_system.search_user(username)
    c = course_system.search_course(refcode)

    print(u)
    print(c)
    if not course_system.add_cart(c, u.get_enrolled_course()):
        return {"Error": "Already enrolled!"}
    else:
        course_system.add_cart(c, u.get_enrolled_course())
        return {"Cart": "Success"}


@app.post("/enroll", tags=["Enrollment"])
async def enroll(enrolled: dict) -> dict:
    pass





