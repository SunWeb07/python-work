'''demonstrate use of lambda function
    to demonstrate user defined module
    demon. class and object /parameterized constructor/constructor
    wap to create employee class withmember variablesemployee name , employee id , salary and experience and display the values to user
    wap to create student class with student name , roll no. ,gender and branch and display values to users by creating constructors(non parameterized constructor)
     
    to greet user by creating class(parameterized constructor)
    to demonstrate default constructor
    to demo. concept of inheritance
    multilevel inheritance
    multiple inheritance
    method overloading/ polymorphism'''

class student:
    name="Sunny"
    rollno=101
    gender="M"
    branch="CSE"
    def __init__(self):
        print("I'm non-parameterzied contructor")
        
    def display(self):
        print(self.name,self.rollno,self.gender,self.branch)
        
        
stu=student()
stu.display()