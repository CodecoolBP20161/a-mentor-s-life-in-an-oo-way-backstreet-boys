from person import Person
import csv

# mentor_csv = open('data/mentors.csv')


class Mentor(Person):
    def __init__(self, nick_name, *args):
        super().__init__(*args)
        self.nick_name = nick_name

    def create_by_csv(self):
        self.mentor_list = []
        with open('data/mentors.csv') as f:
            read_file = csv.reader(f, delimiter='\t')
            mk = []
            i = 0
            for row in read_file:
                data = row[0]
                mk.append(data.split())
                mentor = Mentor(mk[i][0], mk[i][1], mk[i][2], int(mk[i][3]), mk[i][4], int(mk[i][5]), int(mk[i][6]))
                i += 1
                self.mentor_list.append(mentor)
        return self.mentor_list





mentor = Mentor("leves", "Dani", "Daniel", 1234, "male", 10, 10)
# mentor.increase_energy(20)
# mentor.increase_mood(20)
# lista = mentor.create_by_csv()
# print(lista[0].energy)
# lista[0].increase_energy(-15)
# print(lista[0].energy)
