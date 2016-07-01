
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
print("\n")
# input("Press Enter to continue")
# print(codecool_bp.mentors)
for i in codecool_bp.mentors:
    print(i)
print("Mentors are ready")
print("\n")
# input("Press Enter to continue")
for i in codecool_bp.students:
    print(i)
print("Students are ready")
print("\n")
# input("Press Enter to continue")
print(codecool_bp.students[0] + " drank a coffee")
print("Energy of " + codecool_bp.students[0] + " increased from 30 to 55")
print("\n")
# input("Press Enter to continue")
student_knowledges = []
print("the mentors give a briefing about the day")
for i in codecool_bp.students:
    rand = random.randint(20, 50)
    print("Knowledge of " + i + " increased from " + str(rand) + " to " + str(rand + 5))
    student_knowledges.append(rand + 5)
print("\n")
# input("Press Enter to continue")
print("students begin the work with a coding dojo")
j = 0
for i in codecool_bp.students:
    print("Knowledge of " + i + " increased from " + str(student_knowledges[j]) + " to " + str(student_knowledges[j] + 20))
    student_knowledges[j] += 20
    j += 1
print("\n")
# input("Press Enter to continue")
print(codecool_bp.students[4] + " opens facebook")
print("Energy of " + codecool_bp.students[4] + " decreased from " + str(student_knowledges[4]) + " to " + str(student_knowledges[4] - 20))
student_knowledges[4] -= 20
print("\n")
# input("Press Enter to continue")
