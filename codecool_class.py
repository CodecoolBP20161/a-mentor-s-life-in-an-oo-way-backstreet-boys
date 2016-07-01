from mentor import Mentor
from student import Student

class CodecoolClass():

    def __init__(self, location, year, mentors, students):
        mentor = Mentor("leves", "Dani", "Daniel", 1234, "male", 10, 10)
        student = Student("leves", "Dani", "Daniel", 1234, "male", 10, 10)
        lista = mentor.create_by_csv()
        m = []
        for i in range(len(lista)):
            m.append(lista[i].first_name + " " + lista[i].last_name)
        # m = lista[0].first_name + " " + lista[0].last_name
        lista = student.create_by_csv()
        s = []
        for i in range(len(lista)):
            s.append(lista[i].first_name + " " + lista[i].last_name)
        self.location = location
        self.year = year
        self.mentors = m
        self.students = s

    @classmethod
    def generate_local(self):
        pass

    def find_student_by_full_name(self, full_name):
        self.full_name = full_name

    def find_mentor_by_full_name(self, full_name):
        self.full_name = full_name
