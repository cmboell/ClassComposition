"""
Assignment name: Class Composition Assignment
Program: Student.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use a class composition. One class uses information from another class
to display information about a student (getting info from person class) and use functions to change major and update gpa
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    # function to return person info
    def info(self):
        if self.address == '':
            return f'{str(self.first_name)} {str(self.last_name)}'
        else:
            return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.address)}'
