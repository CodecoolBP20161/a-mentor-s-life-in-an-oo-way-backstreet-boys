
from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from events import Events
import random

student = Student("leves", "Laci", "Jocó", 1234, "male", 10, 10)
mentor = Mentor("leves", "Dani", "Daniel", 1234, "male", 10, 10)
codecool_bp = CodecoolClass("Budapest", 2016, student.create_by_csv(), mentor.create_by_csv())
events = Events("fds", "2re", 3)
print("Codecool class generated")
print("Venue: " + codecool_bp.location)
print("Year: " + str(codecool_bp.year))
input("")
# print("\n")
# print(codecool_bp.mentors)
for i in codecool_bp.mentors:
    print(i)
print("Mentors are ready")
input("")
# print("\n")
for i in codecool_bp.students:
    print(i)
print("Students are ready")
input("")
# print("\n")
print(codecool_bp.students[0] + " drank a coffee")
input("")
print("Energy of " + codecool_bp.students[0] + " increased from 30 to 55")
input("")
# print("\n")
student_knowledges = []
print("the mentors give a briefing about the day")
input("")
for i in codecool_bp.students:
    rand = random.randint(20, 50)
    print("Knowledge of " + i + " increased from " + str(rand) + " to " + str(rand + 5))
    student_knowledges.append(rand + 5)
input("")
# print("\n")
print("students begin the work with a coding dojo")
input("")
j = 0
for i in codecool_bp.students:
    print("Knowledge of " + i + " increased from " + str(student_knowledges[j]) + " to " + str(student_knowledges[j] + 20))
    student_knowledges[j] += 20
    j += 1
input("")
# print("\n")
print(codecool_bp.students[4] + " opens facebook")
input("")
print("Knowledge of " + codecool_bp.students[4] + " decreased from " + str(student_knowledges[4]) + " to " + str(student_knowledges[4] - 20))
student_knowledges[4] -= 20
input("")
# print("\n")
print(codecool_bp.students[2] + " reads stack overflow")
input("")
print("Knowledge of " + codecool_bp.students[2] + " increased from " + str(student_knowledges[2]) + " to " + str(student_knowledges[2] + 20))
student_knowledges[2] += 20
input("")
# print("\n")
print(codecool_bp.students[3] + " merges a conflict")
input("")
print("Knowledge of " + codecool_bp.students[3] + " decreased from " + str(student_knowledges[3]) + " to " + str(student_knowledges[3] - 15))
student_knowledges[3] -= 15
input("")
# print("\n")
print(codecool_bp.mentors[1] + " tells a terrible joke")
input("")
j = 0
for i in codecool_bp.students:
    print("Knowledge of " + i + " decreased from " + str(student_knowledges[j]) + " to " + str(student_knowledges[j] - 15))
    student_knowledges[j] -= 15
    j += 1
input("")
# print("\n")
j = 0
print("The day ends, the students finish the day with the following knowledge levels:")
input("")
for i in codecool_bp.students:
    print("Knowledge of " + i + " is " + str(student_knowledges[j]))
    j += 1
