class Person:

    def __init__(self, f_name, l_name, birth_y, gender, mood, energy):
        self.first_name = f_name
        self.last_name = l_name
        self.year_of_birth = birth_y
        self.gender = gender
        self.mood = mood
        self.energy = energy

    def increase_energy(self, delta):
        self.energy += delta
        if delta > 0:
            print("The energy level of %s %s increased by %i" % (self.first_name, self.last_name, delta))
        elif delta < 0:
            print("The energy level of %s %s decreased by %i" % (self.first_name, self.last_name, abs(delta)))
        else:
            print("The energy level of %s %s didn't change" % (self.first_name, self.last_name))
        return delta

    def increase_mood(self, delta):
        self.mood += delta
        if delta > 0:
            print("The mood of %s %s increased by %i" % (self.first_name, self.last_name, delta))
        elif delta < 0:
            print("The mood of %s %s decreased by %i" % (self.first_name, self.last_name, abs(delta)))
        else:
            print("The mood of %s %s didn't change" % (self.first_name, self.last_name))
        return delta

# person = Person("Miki", "Miklos", 1234, "male", 10, 10)
# person.increase_energy(20)
# person.increase_mood(20)
