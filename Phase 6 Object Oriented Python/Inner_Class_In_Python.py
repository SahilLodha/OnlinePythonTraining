from pandas import read_excel


class Student:
    class Faculty:
        def __init__(self, course, sem):
            self.course = course
            self.semester = sem

        def __str__(self):
            return f"Belongs to {self.course}, currently in his/her {self.semester} semester."

    school_name = "Assassins School"

    # Special Methods
    def __init__(self, name, roll, mark1, mark2, mark3, course="Bsc CSIT", sem=0):
        self.name = name
        self.roll = roll
        self.marks = [mark1, mark2, mark3]
        self.faculty = self.Faculty(course, sem)

    def __str__(self):
        return f"Details:\nName:{self.name}\nRoll: {self.roll}\nMarks: {self.marks}\n{self.faculty}"

    # Creating a Instance Method
    # Calculation of average
    def avg(self):
        return sum(self.marks)/3

    # Pass or fail
    def pass_fail(self):
        if False in list(map(lambda x : True if x>40 else False, self.marks )):
            return "Fail"
        else:
            return "Pass"

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


s1 = Student(name="Sahil", roll=421, mark1=75, mark2=78, mark3=81, course="BSc Physics", sem=4)
print("The average of the students is", s1.avg())

print(s1.pass_fail())

print("The School Name:", Student.getSchoolName())
print("The GPS point obtained out of 10: ", Student.convertGPS(s1.avg()))
print("The GPS point obtained out of 10: ", s1.convertGPS(s1.avg()))
print(s1)
