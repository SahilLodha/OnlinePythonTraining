from collections import namedtuple
import csv

"""
This is an example of named tuple and it has multiple benefits
- You have various features of tuple including the features like immutability,
- Increases readability
"""

Points2D = namedtuple('Point', 'x, y')
p = Points2D(1, 2)

# increasing readability example
print(p)
# Using like ordinary tuple | calculating distance from origin
print(p[0]**2 + p[1]**2)
# Using the names to access values | calculating distance from origin
print(p.x**2+p.y**2)

# Other uses of name tuple...
EmployeeRecord = namedtuple("Employee", "f_name, l_name, education, status, salary, address")
employeeRecordList = []

for emp in map(EmployeeRecord._make, csv.reader(open('employee.csv', 'r'))):
    employeeRecordList.append(emp)

print(employeeRecordList)
print(employeeRecordList[1].f_name)
# Viewing all fields of an nametuple
print(employeeRecordList[2]._fields)

# Type casting to ordered dict,
employeeDict = [x._asdict() for x in employeeRecordList]
print(employeeDict)

# creating new tuples from the old nametuples and the field property can be done as shown below
Point3D = namedtuple("Point", Points2D._fields + ('z',))
p = Point3D(1, 2, 3)
print(f"The distance of {p} from origin is {(p.x**2+p.y**2+p.z**2)**0.5}.")
