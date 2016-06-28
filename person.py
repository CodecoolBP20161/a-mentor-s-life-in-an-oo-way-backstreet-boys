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
        return self.energy

    def increase_mood(self, delta):
        self.mood += delta
        return self.mood
