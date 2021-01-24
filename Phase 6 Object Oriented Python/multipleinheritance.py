class Person:
    def __init__(self, fname, lname, date_of_birth, number=None):
        self.first_name = fname
        self.last_name = lname
        self.number = number
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Details are:\nName: {self.first_name} {self.last_name}\nNumber: {self.number}\nDate Of Birth: {self.date_of_birth}"


class Student(Person):
    def __init__(self, fname, lname, number, date_of_birth, roll_no, batch, faculty):
        Person.__init__(self, fname, lname, date_of_birth, number)
        self.roll_no = roll_no
        self.batch = batch
        self.faculty = faculty

    def __str__(self):
        return f'{Person.__str__(self)}\nRoll no.:{self.roll_no}\nBatch: {self.batch}\nFaculty: {self.faculty}'


class Teacher(Person):
    # Creating private variables here.
    __salary = None

    def __init__(self, fname, lname, number, date_of_birth, subject, semester, salary=80000):
        Person.__init__(self, fname, lname, number=number, date_of_birth=date_of_birth)
        self.subject = subject
        self.semesters = semester
        self.__salary = salary

    def __str__(self):
        return f'{Person.__str__(self)}\nSubject: {self.subject}\nGross Salary: {self.__salary}'


teachObj = Teacher('Shreyansh', 'Lodha', 9818651541, '9/16/1996', ['NM', 'DSA'], {'BCA': [1, 4], 'CSIT': [2, 5]})
print(teachObj)
