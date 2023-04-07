from courses import *
from datetime import *
class CourseSystem:
    def __init__(self):
        self.__course_list = []
        self.__user_list = []
        self.__cart = []
        self.__coursecatg_list = []


    # --- User --- #
    def add_user(self, user):
        self.__user_list.append(user)
    def get_user_db(self):
        return self.__user_list
    def delete_user(self):
        pass

    def search_user(self, name):
        username_l = []
        for u in self.__user_list:
            username_l.append(u.get_username())
        if name in username_l:
            return self.__user_list[username_l.index(name)]

    # --- Course --- #
    def create_course(self, created_course):
        self.__course_list.append(created_course)

    def get_course(self):
        return self.__course_list

    def modify_course(self):
        pass

    def delete_course(self, refcode):
        pass
    def search_course(self, name):
        course_l = []
        for c in self.__course_list:
            course_l.append(c.get_refcode())
        if name in course_l:
            return self.__course_list[course_l.index(name)]
    # --- Enroll --- #
    def get_cart(self):
        return self.__cart
    def add_cart(self, will_enrolled, enrolled):
        if will_enrolled in enrolled:
            return False
        else:
            self.__cart.append(will_enrolled)
    def enroll(self, user, cart):
        for i in cart:
            user.set_enrolled_course('enroll', i)
        self.__cart = []

    def browse_course(self, catg):
        for i in self.__course_list:
            if i.get_catg() == catg:
                self.__coursecatg_list.append(i)

        return self.__coursecatg_list
    
course_system = CourseSystem()
course = Courses("SOFT001", "Object Oriented Programming", "Learn writing oop", "teach1", "Software", "All Ages",
                 "To understanding OOP", "10", "10", datetime.now(), "teacher1@gmail.com")
course2 = Courses("HARD001", "Basic Arduino", "Learn Basic Arduino", "teach1", "Hardware", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course3 = Courses("HARD002", "Circuits and Electronics", "Learn Circuit Electronic", "teach1", "Hardware", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course4 = Courses("SOFT002", "Programming Fundamentals", "Learn basic programming", "teach1", "Software", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course5 = Courses("MATH001", "Calculus I", "Learn Calculus I", "teach1", "Math", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course6 = Courses("MATH002", "Calculus II", "Learn Calculus II", "teach1", "Math", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course7 = Courses("MATH003", "Discrete Structure", "Learn Discrete math", "teach1", "Math", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course8 = Courses("SCI001", "Cellular Respiration", "Learn Cellular Respiration", "teach1", "Science", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course9 = Courses("SCI002", "Photosynthesis", "Learn Photosynthesis", "teach1", "Science", "All Ages",
                 "To understanding Arduino", "10", "10", datetime.now(), "teacher1@gmail.com")
course_system.create_course(course)
course_system.create_course(course2)
course_system.create_course(course3)
course_system.create_course(course4)
course_system.create_course(course5)
course_system.create_course(course6)
course_system.create_course(course7)
course_system.create_course(course8)
course_system.create_course(course9)
print(course_system.browse_course("Science"))