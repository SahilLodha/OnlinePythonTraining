from pandas import read_excel


class Faculty:
    def __init__(self, course_name, total_semesters=8, year=4):
        self.course_name = course_name.upper()
        self.total_semesters = total_semesters
        self.year = year

    def __str__(self):
        return f"Course Name: {self.course_name}\nTotal Semester: {self.total_semesters}\nYears: {self.year}"


class Student(Faculty):
    def __init__(self, name, roll,cou_name, total_sem, years,mark1, mark2, mark3):
        Faculty.__init__(self, course_name=cou_name, total_semesters=total_sem, year=years)
        self.name = name
        self.roll_no = roll
        self.marks = [mark1, mark2, mark3]
        self.percentage = self.calc_percen()

    def __str__(self):
        return f"Name: {self.name}\nRoll No: {self.roll_no}\nMarks: {self.marks}\nCourse Name: {self.course_name}" \
               f"\nTotal Semester: {self.total_semesters}\nTotal Year: {self.year}"

    def calc_percen(self):
        return sum(self.marks)/len(self.marks)


s1 = Student(name="Sahil", roll=421, cou_name="BSc. CSIT", total_sem=8, years=4, mark1=56, mark2=76, mark3=99)
print(s1)