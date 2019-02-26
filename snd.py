# Practise Python OOP
# @property
# Student Number Detail
import os

class Student:
    def __init__(self, stuId, stuFName, stuLName):
        self.stuId = stuId
        self.stuFName = stuFName
        self.stuLName = stuLName
    
    # @property function
    @property
    def fullName(self):
        return "{} {}".format(self.stuFName, self.stuLName)
    
    @property
    def joinYear(self):
        return self.stuId[:2]

    @property
    def degree(self):
        return self.stuId[2:4]

    @property
    def syllabus(self):
        return self.stuId[4:6]

    @property
    def studentNumber(self):
        return self.stuId[-3:]

if __name__ == '__main__':
    inputFirstName = input("Input Student First Name: ")
    inputLastName = input("Input Student Last Name: ")
    inputId = input("Input Student ID: ")
    student = Student(inputId, inputFirstName, inputLastName)
    os.system('cls')
    print("Full Name: ", student.fullName)
    print("Join Years: ", student.joinYear)
    print("Degree: ", student.degree)
    print("Syllabus: ", student.syllabus)
    print("Signature ID: ", student.studentNumber)
    
