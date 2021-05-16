'''
1.1	Write a python program to implement Comments, Datatypes, Expressions, Input and Output Functions.

Theory:
A]Comments in python -
    Comments are descriptions that help programmers better understand the intent and functionality of the program.
    They are completely ignored by the Python interpreter.

    Single-line comments: In Python, we use the hash symbol # to write a single-line comment.
    E.g. #this is a single-line comment.

    Multi-line comments: Python doesn't offer a separate way to write multiline comments. However, there are other ways to get around this issue.
    1.Using multiple #
        E.g #this is 
            #a multiline
            #comment.

    2.Using String Literals to write Multi-line Comments :
        Using triple quotes, Here the multiline string isn't assigned to any variable,
        so it is ignored by the interpreter. Even though it is not technically a multiline comment, it can be used as one.
        E.g. this documentation is written using multiline comments.

B]Datatypes in python -
    Every value in Python has a datatype. Since everything is an object in Python programming,
    data types are actually classes and variables are instance (object) of these classes.

    PYTHON NUMBERS
        Integers, floating point numbers and complex numbers fall under Python numbers category.
        They are defined as int, float and complex classes in Python.

    PYTHON STRINGS
        String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings.
        Multi-line strings can be denoted using triple quotes

C]Expressions in python -
    Expressions are representations of value.
    They are different from statement in the fact that statements do something while expressions are representation of value.
    For example any string is also an expressions since it represents the value of the string as well.

D]Input and Output functions -
    python output using print() function :
        We use the print() function to output data to the standard output device (screen). We can also output data to a file.
        E.g. print("Hello world")

    python input using input() function :
        To allow flexibility, we might want to take the input from the user. In Python, we have the input() function to allow this.
        E.g. input("Enter a number:")

@author: KHAN FARHAN NADEEM (19CO27)
'''

i=10
f=10.5
s='aiktc'
print("i=",i,"f=",f,"s=",s)
print("Type of",i,"is",type(i),"Type of",f,"is",type(f),"Type of '",s,"' is",type(s))
print(i,"is at",id(i))
print(f,"is at",id(f))
print(s,"is at",id(s))
print("s=",s," and is at",id(s))
s='co'
print("s=",s," and is at",id(s))
num=int(input("Enter a number:"))
print("num =",num)

'''
Conclusion:
    Comments are description to understand the functionality of program.
    Every datatype is a class in python.
    Expressions are representation of values.
    Input() function is used to take input from user.
    Print() function is used to display output to the user. 
'''