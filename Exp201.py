'''
2.1	Write a python program to implement loops in Python.
Theory

    Python has two primitive loop commands:

    1]The while Loop
        With the while loop we can execute a set of statements as long as a condition is true.
        The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

    2]For loop
        A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
        This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
        With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
        The for loop does not require an indexing variable to set beforehand

    3]The range() Function
        To loop through a set of code a specified number of times, we can use the range() function,
        The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
        The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)

@author: KHAN FARHAN NADEEM (19CO27)
'''

#factorial using for loop
print("Factorial using loop ")
num=int(input('Enter the Number:'))
fact=1
#running the loop in range of number
for i in range(1,num+1):
    # Increasing the value of fact by fact * i
    fact=fact*i 
print('Factorial of',num,'is',fact)

#fibonacci using while loop
print("Fibonacci using loop ")
num=int(input('Enter the Number:'))
a=0
b=1
c=a+b
print('Fibonacci Series till',num,':',a,'\t',b,end='')

#running the loop until condition is false
while(c<=num):
    print("\t",c,end='')
    a=b
    b=c
    c=a+b

'''
Conclusion: 

 Loop is used to repeat a specific block of code a known number of times.
 works more like an iterator method as found in other object-orientated programming languages.
'''