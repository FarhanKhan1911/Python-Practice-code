'''
Program 4.2: Write python program to implement different types of Exceptions.

Thoery:

    ZeroDivisionError: Occurs when a number is divided by zero.
    NameError: It occurs when a name is not found. It may be local or global.
    IndentationError: If incorrect indentation is given.
    IOError: It occurs when Input Output operation fails.
    EOFError: It occurs when the end of the file is reached, and yet operations are being performed.

@author: KHAN FARHAN NADEEM (19CO27)

'''

try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("can't divide by zero")
