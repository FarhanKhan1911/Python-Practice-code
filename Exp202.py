'''
Exp 2.2: Implementation of functions in Python

Thoery

Functions in python

    A function is a block of code which only runs when it is called.
    You can pass data, known as parameters, into a function.
    A function can return data as a result.

    * Creating a Function
        In Python a function is defined using the def keyword

    *Calling a Function
        To call a function, use the function name followed by parenthesis

    *Arguments
        Information can be passed into functions as arguments.
        Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
        The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name

    *Recursion
        Python also accepts function recursion, which means a defined function can call itself.

@author: KHAN FARHAN NADEEM (19CO27)

'''
# Factorial function
def fact(num):
    '''
    Returns the factorial of given number. This is from Session6.py
    '''
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

#Fibonacci Function
def fibo(num):
    a=0
    b=1
    c=a+b
    print('Fibonacci Series upto',num,'is',a,'\t',b,'\t',end='')
    while c<=num:
        print(c,'\t',end='')
        a=b
        b=c
        c=a+b
    print()
    
def fibo1(num):
    a=0
    b=1
    c=a+b
    res=[0,1]
    while c<=num:
        res.append(c)
        a=b
        b=c
        c=a+b
    return res

def main():
    while(True):
        n=int(input('Enter the Number:'))
        print('Factorial of',n,'is',fact(n))
        print('Fibonacci Series upto',n,':',fibo1(n))
        ch=input('\tDo u want to continue (Y/N)?')
        if (ch=='N' or ch=='n'):
            break

if __name__=='__main__':
    main()

'''
conclusion
 
Functions in Python. We use functions in programming to bundle a set of instructions that we want to use repeatedly or that, because of their complexity, are better self-contained in a sub-program and called when needed. That means that a function is a piece of code written to carry out a specified task.
'''