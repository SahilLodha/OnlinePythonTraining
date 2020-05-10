class Student:
    class Faculty:
        def __init__(self, course, sem=0):
            self.course = course
            self.semester = sem

        def __str__(self):
            return f"Belongs to {self.course}, currently in his/her {self.semester} semester."

    school_name = "Assassins School"

    # Special Methods
    def __init__(self, name, roll, mark1, mark2, mark3, course="Bsc CSIT"):
        self.name = name
        self.roll = roll
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.faculty = self.Faculty(course)

    def __str__(self):
        return f"Details:\nName:{self.name}\nRoll: {self.roll}\nMarks: [{self.mark1}, {self.mark2}, {self.mark3}]\n{self.Faculty.__str__(self.faculty)}"

    # Creating a Instance Method
    # Calculation of average
    def avg(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    # Pass or fail
    def pass_fail(self):
        if self.mark1 > 40 and self.mark2 > 40 and self.mark3 > 40:
            return True
        else:
            return False

    # Creating a class Method
    # def info(cls):
    #     return cls.school_name

    @classmethod
    def getSchoolName(cls):
        return cls.school_name

    # Static Method
    @staticmethod
    def convertGPS(average):
        return average / 10


s1 = Student(name="Sahil", roll=421, mark1=75, mark2=78, mark3=81)
print("The average of the students is", s1.avg())

if s1.pass_fail():
    print("Passed")
else:
    print('Failed')

print("The School Name:", Student.getSchoolName())
print("The GPS point obtained out of 10: ", Student.convertGPS(s1.avg()))
print("The GPS point obtained out of 10: ", s1.convertGPS(s1.avg()))
print(s1)
