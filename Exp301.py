'''Experiment 3 
3.1: Program to implement Class, objects and static method

Theory

1]Python Classes/Objects

    Python is an object oriented programming language.
    Almost everything in Python is an object, with its properties and methods.
    A Class is like an object constructor, or a "blueprint" for creating objects.

    *Create a Class
        To create a class, use the keyword class

    *Object Methods
        Objects can also contain methods. Methods in objects are functions that belong to the object

    *The self Parameter
        The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class

@author: KHAN FARHAN NADEEM (19CO27)
'''

class Student:
    '''
    A Student class to maintain students information.
    It has class variables and also instance variables.
    '''
    # class variable
    no_of_courses=5 
    credits=25         
    
    def setval(self,rollno,name,addr,mob):
        '''
        Method to set the properties of the object.
        '''
        #Instance variable
        self.rollno=rollno      
        self.name=name
        self.addr=addr
        self.mob=mob
    def getval(self):
        print('Self is at',id(self))
        return self.rollno, self.name, self.no_of_courses, self.credits, self.mob
        
    @classmethod            #decorator
    # Method to setcourse
    def setcourses(cls,n):
        cls.no_of_courses=n
    @classmethod
    # Method to set credits
    def setcredits(cls,c):
        cls.credits=c
    @staticmethod
    # Method to check whether it is workday or not
    def is_workday(day):
        if day.weekday()==6:
            return False
        return True

#main function
def main():
    #calling Student class
    s=Student()
    s.setval('19CO10','Ansari Wasim','Panvel',9898929292)
    print(s.getval())
    s.setcourses(7)
    print(s.getval())
    s1=Student()
    s1.setval('19CO20','Khan Wasim','Mumbai',9898929292)
    print(s1.getval())
    s1.setcredits(30)
    print(s.getval())
    print(s1.getval())
    import datetime
    d=datetime.date(2021,2,28)
    print('Is workday ?',Student.is_workday(d))
  

    #calling Student class
    s1=Student()
    s1.setval('19CO01','Ansari Ahmed','Mumbai',9898998989)
    #print('s1 is at',id(s1))
    print(s1.getval())
    #print(s1.setval.__doc__)
    s2=Student()
    Student.setcourses(6)
    s2.setval('19CO02','Muskan','Mumbai',9898998989)
    #print('s2 is at',id(s2))
    print(s2.getval())
    Student.setcredits(30)
    
    print(s1.getval())
    import datetime
    d=datetime.date(2021,2,26)
    print('Is workday ?',Student.is_workday(d))


if __name__=='__main__':
    main()

'''
conclusion
 A Python class is for defining a particular type of object. Because Python objects can have both function and data elements, Python classes define what methods can be used to change the state of an object. They also indicate what attributes the object can have.

'''