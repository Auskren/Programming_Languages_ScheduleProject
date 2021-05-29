

# check is teacher busy in time slot
def isBusy(instructor, day, time, busy):
    for x in busy:
        if instructor == x.teacher and day == x.day and time == str.rstrip(x.time):
            return bool(1)
    return bool(0)


# get course from courses.csv
def getCourse(course_name, courses):
    for course in courses:
        if course_name == course.course:
            return course


# get course index from courses.csv
def getCourseIndex(course_name, courses):
    courseindex = 0
    for course in courses:
        if course_name == course.course:
            return courseindex
        else:
            courseindex = courseindex + 1


# in one time slot there can be one
# semester classes therefore before adding to lessons
# we have to check is alredy exist in that day
def semesterContain(array, _semester):
    for obj in array:
        if obj.semester == _semester:
            return bool(1)
    return bool(0)

