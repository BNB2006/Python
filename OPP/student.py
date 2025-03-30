# Q3. Write a program to create one parent class “Registration” having variables name, enrollno, branch and class,
# also having one function to display values of all variables. Then create one child class which don’t have any
# variable, create object of that class and display all registration details

class Registration:
    def __init__(self, sName, sRollNo, sBranch, sClass):
        self.name = sName
        self.enrollno = sRollNo
        self.branch = sBranch
        self.stu_class = sClass
    
    def details(self):
        print(f"Student Name: {self.name}")
        print(f"Student Enrollment No: {self.enrollno}")
        print(f"Student Branch: {self.branch}")
        print(f"Student Class: {self.stu_class}")
        return
    
class Student(Registration):
    pass

def main():
    child = Student("Balaji", "2307003", "IT", "2nd")
    child.details()

if __name__ == main():
    main()