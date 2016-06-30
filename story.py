from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from events import Events

student = Student("leves", "Laci", "Jocó", 1234, "male", 10, 10)
lista1 = student.create_by_csv()
mentor = Mentor("leves", "Dani", "Daniel", 1234, "male", 10, 10)
lista = mentor.create_by_csv()
codecool_bp = CodecoolClass("Budapest", 2016, student.create_by_csv(), mentor.create_by_csv())
print("Codecool class generated")
print("Venue: " + codecool_bp.location)
print("Year: " + str(codecool_bp.year))
# input("Press Enter to continue")
print("Mentors are ready")
print(codecool_bp.mentors)
