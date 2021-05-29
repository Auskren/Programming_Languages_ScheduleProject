import itertools
import eel
from classes import *
from backendFunctions import *


@eel.expose
def calculate(courseFileName: str, busyFileName: str, classroomFileName: str, serviceFileName: str):
    courses = []
    with open(courseFileName) as fp:
        line = fp.readlines()
    for data in line:
        token = data.split(";")
        s = Courses(token[0], token[1], token[2], token[3], token[4], token[5], str.rstrip(token[6]))
        courses.append(s)

    busy = []
    with open(busyFileName) as fp:
        line = fp.readlines()
    for data in line:
        token = data.split(";")
        s = Busy(token[0], token[1], token[2])
        busy.append(s)

    classroom = []
    with open(classroomFileName) as fp:
        line = fp.readlines()
    for data in line:
        token = data.split(";")
        s = Classroom(token[0], token[1])
        classroom.append(s)

    service = []
    with open(serviceFileName) as fp:
        line = fp.readlines()
    for data in line:
        token = data.split(";")
        s = Service(token[0], token[1], token[2])
        service.append(s)

    # creating day arrays which contains courses object
    mondayMorning = []
    mondayAfternoon = []

    tuesdayMorning = []
    tuesdayAfternoon = []

    wednesdayMorning = []
    wednesdayAfternoon = []

    thursdayMorning = []
    thursdayAfternoon = []

    fridayMorning = []
    fridayAfternoon = []

    # create day object and set empty arrays
    monday = Day("Monday", mondayMorning, mondayAfternoon)
    tuesday = Day("Tuesday", tuesdayMorning, tuesdayAfternoon)
    wednesday = Day("Wednesday", wednesdayMorning, wednesdayAfternoon)
    thursday = Day("Thursday", thursdayMorning, thursdayAfternoon)
    friday = Day("Friday", fridayMorning, fridayAfternoon)

    # create days array to get dynamic operation and try different fit positions if there is not exist
    days = [monday, tuesday, wednesday, thursday, friday]

    # set fixed service courses automatically
    for obj in service:
        for day in days:
            if obj.day == day.day:
                if obj.time == "Morning":
                    day.morning.append(getCourse(obj.name, courses))
                    if getCourse(obj.name, courses).comp_or_elective == "E":
                        day.bigCountM += 1
                        courses.pop(getCourseIndex(obj.name, courses))
                    else:
                        day.smallCountM += 1
                        courses.pop(getCourseIndex(obj.name, courses))
                else:
                    day.afternoon.append(getCourse(obj.name, courses))
                    if getCourse(obj.name, courses).comp_or_elective == "E":
                        day.bigCountA += 1
                        courses.pop(getCourseIndex(obj.name, courses))
                    else:
                        day.smallCountA += 1
                        courses.pop(getCourseIndex(obj.name, courses))

    numberOfRooms = 0
    for obj in classroom:
        numberOfRooms += int(obj.number)

    counter = 0
    index = 0
    # while len courses != 0 means every element in that array must be placed a fit position
    while len(courses) != 0:
        for day in days:  # search days
            # dynamic
            # for example in monday we have to set lessons until fully positioned in to morning and afternoon
            while day.smallCountA + day.bigCountA + day.smallCountM + day.bigCountM < 2 * numberOfRooms and index < len(
                    courses):
                isBusyTeacher = isBusy(courses[index].instructor, day.day, "Afternoon", busy) and isBusy(
                    # check teacher is all day busy
                    courses[index].instructor, day.day, "Morning", busy)
                isBusyAfternoon = isBusy(courses[index].instructor, day.day,
                                         "Afternoon", busy)  # check is teacher busy in afternoon
                isBusyMorning = isBusy(courses[index].instructor, day.day,
                                       "Morning", busy)  # check is teacher busy in morning
                if courses[index].comp_or_elective == 'C' and not isBusyTeacher:
                    # check is compulsory and teacher is not busy
                    # if morning is empty and there is not exist same semester
                    if len(day.morning) < 3 and not isBusyMorning and not semesterContain(day.morning,
                                                                                          courses[index].semester):
                        day.morning.append(courses[index])
                        day.bigCountM += 1
                        courses.pop(index)
                    elif len(day.afternoon) < 3 and not isBusyAfternoon and not semesterContain(day.afternoon,
                                                                                                courses[
                                                                                                    index].semester):
                        day.afternoon.append(courses[index])
                        day.bigCountA += 1
                        courses.pop(index)
                    else:
                        index += 1
                # check is elective or not
                elif courses[index].comp_or_elective == 'E' and not isBusyTeacher:
                    if len(day.morning) < 3 and not isBusyMorning:
                        day.morning.append(courses[index])
                        day.smallCountM += 1
                        courses.pop(index)
                    elif len(day.afternoon) < 3 and not isBusyAfternoon:
                        day.afternoon.append(courses[index])
                        day.smallCountA += 1
                        courses.pop(index)
                    else:
                        index += 1
                else:
                    index = index + 1
        # after we search and set elements all of days get another permutation of array
        if len(courses) != 0:
            counter += 1
            itertools.permutations(days, counter)
            index = 0
        if counter == 1000:
            break
    output = ""
    for d in days:
        for obj in d.morning:
            output+= d.day + ";" + "m;" + obj.instructor + ";" + obj.course + ";" + obj.comp_or_elective + "\n"

        for obj in d.afternoon:
            output+= d.day + ";" + "a;" + obj.instructor + ";" + obj.course + ";" + obj.comp_or_elective + "\n"

    eel.printer(output)
