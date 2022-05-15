#single
class country:
    def __init__(self,name,capital):
        self.name=name
        self.capital=capital
    def display(self):
        print(self.name,self.capital)
class state(country):
    def __init__(self,name,capital,sname,scapital):
        self.sname=sname
        self.scapital=scapital
        country.__init__(self,name,capital)
    def dissplay(self):
        print(self.sname,self.scapital)
hyd=state("india","dehli","telangana","hyderabad")
hyd.display()
hyd.dissplay()
#multiple level
# parent class
class Student():
   # constructor of parent class
   def __init__(self, name, enrollnumber):
      self.name = name
      self.enrollnumber = enrollnumber
   def display(self):
      print(self.name)
      print(self.enrollnumber)
# child class
class College( Student ):
   def __init__(self, name, enrollnumber, admnyear, branch):
      self.admnyear = admnyear
      self.branch = branch
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)
# child class
class University( Student ):
   def __init__(self, name, enrollnumber, refno, branch):
      self.refno = refno
      self.branch = branch
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)
# creation of an object for base/derived class
obj_1 = College('sun',42414802718,2018,"CSE")
obj_1.display()
obj_2 = University ('sun',42414802718,"st2018","CSE")
obj_2.display()
#multilevel
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread…")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat() 