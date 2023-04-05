class CourseSystem:
    def __init__(self):
        self.__course_list = []
        self.__user_list = []
        
    def add_user(self, user):
        self.__user_list.append(user) 
    def delete_user(self):
        pass       
        
    def search_user(self, name):
        for u in self.__user_list:
            if u.name == name:
                return u              
             
    def create_course(self, created_course):
        self.__course_list.append(created_course)
    def get_course(self):
        return self.__course_list
    def modify_course(self):
        pass
    def delete_course(self, refcode):
        pass
    

# --- Course Object --- #
class Courses:
    def __init__(self, refcode, title, desc, teacher, catg, target, objective, hour, recom_hour, release, contact):
        self.__refcode = refcode
        self.__title = title
        self.__desc = desc
        self.__teacher = teacher
        self.__catg = catg
        self.__target = target
        self.__objective = objective
        self.__hour = hour
        self.__recom_hour = recom_hour
        self.__release = release
        self.__contact = contact
        
    def get_refcode(self):
        return self.__refcode

    def get_title(self):
        return self.__title

    def get_desc(self):
        return self.__desc

    def get_teacher(self):
        return self.__teacher

    def get_catg(self):
        return self.__catg

    def get_target(self):
        return self.__target

    def get_objective(self):
        return self.__objective

    def get_hour(self):
        return self.__hour

    def get_recom_hour(self):
        return self.__recom_hour

    def get_release(self):
        return self.__release

    def get_contact(self):
        return self.__contact

class CourseCatg:
    pass


# --- Course Material --- #
class CourseChapter:
    pass


class CourseMaterial:
    pass


class CourseExam:
    def __init__(self,course_name,exam_list,ans_list):
        self._course_name = course_name
        self._exam_list = exam_list
        self._ans_list = ans_list
    def do_exam(self):
        pass
    def ans_check(self):
        pass
            
            
class CouseProgression:
    def __init__(self):
        pass
