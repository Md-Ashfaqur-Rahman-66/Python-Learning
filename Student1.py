class Student1:
    def __init__(self, name, major, gpa):
        self.name = name    #The name of the student will the name that we passed in
        self.major = major  #The major of the student will the major that we passed in
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False