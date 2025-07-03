class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        print(f"name is {self.name}, email:{self.email}")
    def set_email(self, new_email):
        self.__email = new_email
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled_courses = []
    def enroll(self, course_name):
        self.__enrolled_courses.append(course_name)
    def get_enrolled_courses(self):
        return self.__enrolled_courses
class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__teaching_courses = []
    def add_course(self, course_name):
        self.__teaching_courses.append(course_name)
    def get_teaching_courses(self):
        return self.__teaching_courses