
# Create classes to set value of from sources
class Service:
    def __init__(self, name, day, time):
        self.name = name
        self.day = day
        self.time = time


class Classroom:
    def __init__(self, size, number):
        self.size = size
        self.number = number


class Busy:
    def __init__(self, teacher, day, time):
        self.teacher = teacher
        self.day = day
        self.time = time


class Courses:
    def __init__(self, course, course_name, semester, credit, comp_or_elective, dep_or_service, instructor):
        self.course = course
        self.course_name = course_name
        self.semester = semester
        self.semester = semester
        self.credit = credit
        self.comp_or_elective = comp_or_elective
        self.dep_or_service = dep_or_service
        self.instructor = instructor


class Day:
    def __init__(self, day, morning, afternoon):
        self.day = day
        self.morning = morning
        self.afternoon = afternoon
        self.bigCountM = 0
        self.smallCountM = 0
        self.bigCountA = 0
        self.smallCountA = 0




class Lesson:
    def __init__(self, day, time, cls, courseName):
        self.day = day
        self.time = time
        self.cls = cls
        self.courseName = courseName

