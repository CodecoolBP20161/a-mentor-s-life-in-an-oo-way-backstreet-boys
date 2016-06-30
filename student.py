from person import Person
import csv

class Student(Person):
    def __init__(self, knowledge, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.knowledge = knowledge

    def increase_knowledge(self, delta):
        self.knowledge += delta
        if delta > 0:
            print("The knowledge of %s %s increased by %i" % (self.first_name, self.last_name, delta))
        elif delta < 0:
            print("The knowledge of %s %s decreased by %i" % (self.first_name, self.last_name, abs(delta)))
        else:
            print("The knowledge of %s %s didn't change" % (self.first_name, self.last_name))
        return delta

    def create_by_csv(self):
        self.student_list = []
        with open('data/students.csv') as f:
            read_file = csv.reader(f, delimiter='\t')
            mk = []
            i = 0
            for row in read_file:
                data = row[0]
                mk.append(data.split())
                student = Student(int(mk[i][0]), mk[i][1], mk[i][2], int(mk[i][3]), mk[i][4], int(mk[i][5]), int(mk[i][6]))
                i += 1
                self.student_list.append(student)
        return self.student_list

# student = Student("leves", "Laci", "Jocó", 1234, "male", 10, 10)
# lista1 = student.create_by_csv()
# print(lista1[0].energy)
