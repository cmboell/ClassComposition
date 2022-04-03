"""
Assignment name: Class Composition Assignment
Program: Student.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use a class that inherits from another class to display information about a
student (which inherits from Person) and use functions to change major and update gpa
"""

# import
from class_definitions.Person import Person


# student class
class Student:
    def __init__(self, person, major, start_date, gpa):
        self.person = person
        self.major = major
        self.start_date = start_date
        self.gpa = gpa

    # function to change major
    def change_major(self, major):
        self.major = major

    # function to update gpa
    def update_gpa(self, gpa):
        self.gpa = gpa

    def display(self):
        return f'{str(self.person.info())}\n{str(self.major)}\n{str(self.start_date)}\n{float(self.gpa)}'


# Driver code
if __name__ == '__main__':
    p = Person('Boell', 'Colby')
    s = Student(p, 'Computer Information Systems', 'August 28, 2020', 4.0)
    print(s.display())
    s.change_major('Being Awesome')
    s.update_gpa(3.0)
    print(s.display())

