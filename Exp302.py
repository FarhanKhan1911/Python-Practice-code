'''
Experiment 3
3.2 : Write a python program to implement Constructors

Theory 

    Constructors:
        Constructors are generally used for instantiating an object.The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
        In Python the __init__() method is called the constructor and is always called when an object is created.

        *Types of constructors :

        1]default constructor :The default constructor is simple constructor which doesn’t accept any arguments.It’s definition has only one argument which is a reference to the instance being constructed.

        2]parameterized constructor :constructor with parameters is known as parameterized constructor.The parameterized constructor take its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

    *The __init__() Function:

        All classes have a function called __init__(), which is always executed when the class is being initiated.
        Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

@author: KHAN FARHAN NADEEM (19CO27)
'''
#Student Class
class Student:
    no_of_courses=5
    credits=25
    
    #constructor 
    def __init__(*arg):
        if(len(arg)>1):
            if isinstance(arg[1],Student):
                #instance variable
                arg[0].rollno=arg[1].rollno   
                arg[0].name=arg[1].name
                arg[0].addr=arg[1].addr
                arg[0].mob=arg[1].mob
            else:
                arg[0].rollno=arg[1]   #instance var
                arg[0].name=arg[2]
                arg[0].addr=arg[3]
                arg[0].mob=arg[4]
        else:
            arg[0].rollno=arg[0].name=arg[0].addr=arg[0].mob=None
    
    def setval(self,rollno,name,addr,mob):
        self.rollno=rollno
        self.name=name
        self.addr=addr
        self.mob=mob
    def getval(self):
        return self.rollno, self.name, self.no_of_courses, self.credits, self.mob, id(self)
    @classmethod
    def setcourses(cls,n):
        cls.no_of_courses=n
    @classmethod
    def setcredits(cls,c):
        cls.credits=c
    @staticmethod
    def is_workday(day):
        if day.weekday()==6:
            return False
        return True

#main function
def main():
    s=Student('19CO50','Khan Aftab','New Panvel',9898989898)
    print(s.getval())
    s.setcourses(7)
    print(s.getval())
    s1=Student()
    print(s1.getval())
    s1.setcredits(30)
    print(s.getval())
    print(s1.getval())
    import datetime
    d=datetime.date(2021,3,3)
    print('Is workday ?',Student.is_workday(d))
    s2=Student(s1)
    print(s2.getval())
    s3=s1
    print(s3.getval())


if __name__=='__main__':
    main()

'''
Conclusion:
    The purpose of constructor is to initialize the object of a class
    Constructors do not have return types while methods do.
    constructor is used to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts.
'''