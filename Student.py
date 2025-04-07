class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name    #The name of the student will the name that we passed in
        self.major = major  #The major of the student will the major that we passed in
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False