from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from events import Events


codecool_bp = CodecoolClass("Budapest", 2016, Student.create_by_csv, Mentor.create_by_csv())
print("Codecool class generated")
print("Venue: " + codecool_bp.location)
print("Year: " + str(codecool_bp.year))
input("Press Enter to continue")
print("Mentors are ready")
