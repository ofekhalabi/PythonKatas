from asyncio import ReadTransport


def can_enroll(student, course):
    """
    Checks if a student can enroll in a course based on their grade level and the course's grade requirement.
    """
    return student["grade_level"] >= course['grade_requirement']


student = {'name': 'Bob', 'grade_level': 9}
course = {'title': 'Advanced Mathematics', 'grade_requirement': 10}


result = can_enroll(student, course)
print(result)  # True expected

"""
To complete this exercise:
--------------------------
No any implementation notes.
"""
