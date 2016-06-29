from person import Person


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
