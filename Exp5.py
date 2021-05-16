'''
5: Write a program to demonstrate the Implementation of Stack, Queue and Linked List

Thoery 

1]Stack
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
In stack, a new element is added at one end and an element is removed from that end only.
The insert and delete operations are often called push and pop.

The functions associated with stack are:

empty() – Returns whether the stack is empty – Time Complexity : O(1)
size() – Returns the size of the stack – Time Complexity : O(1)
top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
pop() – Deletes the top most element of the stack – Time Complexity : O(1)

* Stack in Python can be implemented using following ways: 

a]list
b]collections.deque
c]queue.LifoQueue

2]Queue

Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner.
With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

*Operations associated with queue are: 
 
1]Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
2]Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
3]Front: Get the front item from queue – Time Complexity : O(1)
4]Rear: Get the last item from queue – Time Complexity : O(1)

*Queue in Python can be implemented by the following ways:
 
a]list
b]collections.deque
c]queue.Queue


3]Linked List

A linked list is a sequence of data elements, which are connected together via links.
Each data element contains a connection to another data element in form of a pointer. Python does not have linked lists in its standard library. 
A linked list is created by using the node class.

    *Traversing a Linked List
Singly linked lists can be traversed in only forwrad direction starting form the first data element.
We simply print the value of the next data element by assgining the pointer of the next node to the current data element.

    *Insertion in a Linked List
Inserting element in the linked list involves reassigning the pointers from the existing nodes to the newly inserted node.
Depending on whether the new data element is getting inserted at the beginning or at the middle or at the end of the linked list,

    *Removing an Item form a Liked List
We can remove an existing node using the key for that node.
In the below program we locate the previous node of the node which is to be deleted.
Then point the next pointer of this node to the next node of the node to be deleted.

@author: KHAN FARHAN NADEEM (19CO27)
'''

from os import system, name  
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

class Stack:
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
        print(f"\t\t{val} inserted\n\n")
    def display(self):
        print(*self.data)
    def remove(self):
        if len(self.data) == 0:
            print("\t\tStack Empty\n\n")
        else:
            print(self.data.pop(len(self.data)-1),"\t\t removed\n\n")

class Queue:
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
        print(f"\t\t{val} inserted\n\n")
    def display(self):
        print(*self.data)
    def remove(self):
        if len(self.data) == 0:
            print("\t\tQueue Empty\n\n")
        else:
            print(self.data.pop(0),"\t\t removed\n\n")

class Node:
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.next = nextNode

class linkedList:
    def __init__(self,):
        self.head = None

    def insert(self,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode

        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        print(f"\t\t Node added with value {data} \n\n")

    def display(self):
        if self.head==None:
            print('\t\tLinked List is Empty.\n\n')
        else:
            temp=self.head
            print('\t\t\nLinked List Contents:')
            while temp:
                print("\t\t",temp.data)
                temp=temp.next

    def remove(self):
        prev = self.head
        temp = self.head
        if self.head == None:
            print("\t\t\nLinked list empty\n\n")
        elif self.head.next == None:
            self.head = None
        else:
            while temp.next != None:
                prev = temp
                temp = temp.next

            prev.next = None
            print("\t\tNode removed\n\n")




def stackFun():
    st = Stack()
    while True:
        print("\t Stack Function")
        print("\t\t+=======================+")
        print("\t\t| Number |    Command   |")
        print("\t\t|   1    |    Insert    |")
        print("\t\t|   2    |      Pop     |")
        print("\t\t|   3    |    Display   |")
        print("\t\t|   4    |   Go To menu |")
        print("\t\t+=======================+")
        a = int(input("Enter the number to execute command : "))
        if a == 1:
            try:
                data = int(input("Enter the number :"))
            except:
                print("Enter Integer Number Only")
            st.push(data)
        elif a == 2:
            st.remove()
        elif a==3:
            st.display()
        elif a == 4:
            return False
        else:
            print("InValid Command")

def linkedlistFun():
    st = linkedList()
    while True:
        print("\t Linked list Function")
        print("\t\t+=======================+")
        print("\t\t| Number |    Command   |")
        print("\t\t|   1    |    Insert    |")
        print("\t\t|   2    |      Pop     |")
        print("\t\t|   3    |    Display   |")
        print("\t\t|   4    |   Go To menu |")
        print("\t\t+=======================+")
        a = int(input("Enter the number to execute command : "))
        if a == 1:
            try:
                data = int(input("Enter the number :"))
            except:
                print("Enter Integer Number Only")
            st.insert(data)
        elif a == 2:
            st.remove()
        elif a==3:
            st.display()
        elif a == 4:
            return False
        else:
            print("InValid Command")

def queueFun():
    st = Queue()
    while True:
        print("\t Queue Function")
        print("\t\t+=======================+")
        print("\t\t| Number |    Command   |")
        print("\t\t|   1    |    Insert    |")
        print("\t\t|   2    |      Pop     |")
        print("\t\t|   3    |    Display   |")
        print("\t\t|   4    |   Go To menu |")
        print("\t\t+=======================+")
        a = int(input("Enter the number to execute command : "))
        if a == 1:
            try:
                data = int(input("Enter the number :"))
            except:
                print("Enter Integer Number Only")
            st.push(data)
        elif a == 2:
            st.remove()
        elif a==3:
            st.display()
        elif a == 4:
            return False
        else:
            print("InValid Command")

def main():
    clear()
    print("\t Menu driven program for data structure ")
    print("\t\t+====================+")
    print("\t\t|  1  |    Stack     |")
    print("\t\t|  2  |  Linked List |")
    print("\t\t|  3  |     queue    |")
    print("\t\t|  4  |     exit     |")
    print("\t\t+====================+")
    cmd = int(input("Enter the number : "))
    if cmd == 1:
        clear()
        stackFun()
    elif cmd == 2:
        clear()
        linkedlistFun()
    elif cmd == 3:
        clear()
        queueFun()
    elif cmd == 4:
        exit()
while True:
    main()
    
'''
conclusion:
A stack is a data structure used to store a collection of objects. Individual items can be added and stored in a stack using a push operation.
To add an element to the queue, use put() . This is called an enqueue operation.
To remove an element from the queue, use get() . This is called a dequeue operation.
The FIFO (First In, First Out) principle means the first element you insert will also be the first to be removed.
Linked lists are often used because of their efficient insertion and deletion. They can be used to implement stacks, queues, and other abstract data types.
'''    

