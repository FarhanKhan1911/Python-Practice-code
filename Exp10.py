'''
Exp 10: Program on Threading using python.

Theory:
In computing, a process is an instance of a computer program that is being executed.
Any process has 3 basic components:

An executable program.
The associated data needed by the program (variables, work space, buffers, etc.)
The execution context of the program (State of process)
A thread is an entity within a process that can be scheduled for execution.
Also, it is the smallest unit of processing that can be performed in an OS (Operating System).
In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity,
you can assume that a thread is simply a subset of a process!

A thread contains all this information in a Thread Control Block (TCB):
Thread Identifier: Unique id (TID) is assigned to every new thread
Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
Program counter: a register which stores the address of the instruction currently being executed by thread.
Thread state: can be running, ready, waiting, start or done.
Thread’s register set: registers assigned to thread for computations.
Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.

Multiple threads can exist within one process where:
Each thread contains its own register set and local variables (stored in stack).
All thread of a process share global variables (stored in heap) and the program code.
Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
In Python, the threading module provides a very simple and intuitive API for spawning multiple threads in a program.

@author: KHAN FARHAN NADEEM (19CO27)
'''

from threading import *
from time import sleep

class A(Thread):
    def run(self):
        for i in range(50):
            print('A')

class B(Thread):
    def run(self):
        for i in range(50):
            print('B')


def main():
    a = A()
    b = B()
    a.start()
    sleep(0.1)
    b.start()
    a.join()
    b.join()
    print('Done')

if __name__=='__main__':
    main()

'''
Conclusion:
It Enhances performance by decreased development time.
It Simplifies and streamlines program coding and improves GUI responsiveness.
It helps to use CPU resource in a better way.
'''