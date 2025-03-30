""" Q2. Write a program to create a class Employee having to variables empid, empname and empdesg.
 Also having two functions , one for taking input and another to display data. Create three objects for Employee class"""

class Employee:
    def __init__(self):
         self.empId = None
         self.empName = None
         self.empdesg = None


    def takeInput(self):
         id = int(input("\nEnter the employee Id: "))
         name = input("Enter the name of Employee: ")
         desg = input("Enter designation of Employee: ")
         self.empId = id
         self.empName = name
         self.empdesg = desg
         return
    

    def empData(self):
         print(f"Employee Id :{self.empId}")
         print(f"Employee Name: {self.empName}")
         print(f"Employee designation: {self.empdesg}\n")



def main():
    e1 = Employee()
    e2 = Employee()
    e3 = Employee()

    print("Employee 1:")
    e1.takeInput()
    print("Employee 2:")
    e2.takeInput()
    print("Employee 3:")
    e3.takeInput()

    e1.empData()
    e2.empData()
    e3.empData()

if __name__ == main():
     main()