from mentor import Mentor
from student import Student


class CodecoolClass():

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = []
        self.students = []

    @classmethod
    def generate_local(self):
        pass

    def find_student_by_full_name(self, full_name):
        self.full_name = full_name

    def find_mentor_by_full_name(self, full_name):
        self.full_name = full_name
