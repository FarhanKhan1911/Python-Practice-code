'''
Program 4.1: Write a program to demonstrate Implementation of Inheritance

Thoery:

Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

*Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class

*Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class

*Add the __init__() Function
we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).

 The __init__() function is called automatically every time the class is being used to create a new object.

@author: KHAN FARHAN NADEEM (19CO27)

'''

# Inheritance 
class Person:
    def __init__(self,n=None,a=None,m=None):
        self.name=n
        self.addr=a
        self.mob=m
    def getval(self):
        return self.name,self.addr,self.mob

class Student(Person):
    def __init__(self,r=None,n=None,a=None,m=None,sgpi=None):
        self.rollno=r
        self.sgpi=sgpi
        Person.__init__(self,n,a,m)     #initialize the instance vars inherited from base class
    def getstud(self):
        return self.rollno,self.name,self.sgpi


#driver code
print("#  Inheritance #")
p=Person('Ahmed','Mumbai',9898989898)
print(p.getval())
s=Student('19CO45','Sachin','Panvel',989898,8.8)
print(s.getstud())

# Polymorphism 

class Bird:
  def intro(self):
    print("There are many types of birds.")
      
  def flight(self):
    print("Most of the birds can fly but some cannot.")
    
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
      
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
      
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()

'''
Conclusion
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Inheritance allows programmers to create classes that are built upon existing classes, to specify a new implementation while maintaining the same behaviors (realizing an interface), to reuse code and to independently extend original software via public classes and interfaces.

'''