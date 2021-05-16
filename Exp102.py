'''
1.2	Write a python program to implement List, Set, Tuple, Dictionary and Array.
Theory

    There are four collection data types in the Python programming language:
    1]List is a collection which is ordered and changeable. Allows duplicate members.
    2]Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    3]Set is a collection which is unordered and unindexed. No duplicate members.
    4]Dictionary is a collection which is ordered* and changeable. No duplicate members.

@author: KHAN FARHAN NADEEM (19CO27)
 
'''
from array import *

'''
List Theory:
    Lists are used to store multiple items in a single variable.

    Lists are one of 4 built-in data types in Python used to store collections of data
    List items are ordered, changeable, and allow duplicate values.
    List items are indexed, the first item has index [0], the second item has index [1]
    List items are indexed and you can access them by referring to the index number
'''
print( "---------------LIST -----------------")
print("")

#Creating a list of variable datatypes
l=[12,23,-5,0.8,'python',"CO"] 

#printing list
print("printing original list",l) 

#printing first three elements of a list
print("printing first three elements of a list", l[0:3]) 

#printing Last elements of a list
print("printing Last elements of a list",l[-1]) 

#printing first three elements of a list twice
print("printing first three elements of a list twice",l[0:3] * 2) 

print ("\n--------------LIST FUNCTIONS-----------------\n")

#Creating a list of range 1 to 7
l1=list(range(1,8)) 

print ("List of range 1 to 7", l1)
#append 9
l1.append(9) 
print ("Append 9 :",l1)
#sorting the list in reverse order (descending order)
l1.sort(reverse=True)
print("Descending Sort:",l1)
#sorting the list in reverse order (ascending order)
l1.sort()
print ("Ascending Sort:",l1)
l1.reverse()
print("Reverse:",l1)
l1.sort()
l1.remove(9)

print("Remove 9:",l1)
print("count:",l1.count(5))
print("max:",max(l1))
print("min:",min(l1))
print("Index of 6:",l1.index(6))

'''
Tuple Theory
    Tuples are used to store multiple items in a single variable.
    Tuple is one of 4 built-in data types in Python used to store collections of data
    A tuple is a collection which is ordered and unchangeable.
    Tuples are written with round brackets.
    Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [0], the second item has index [1]

'''
print("--------TUPLE DATATYPE (READ ONLY LIST)------------")
print("")

#Creating a Tuple
tpl=(-5,0.8,'python',"CO") 
print("Created Tuple is ", tpl)

#printing first two elements of a touple
print("Tuple elements 0 to 2 is", tpl[0:2]) 
print("")
print("--------TUPLE FUNCTIONS -----------")

#Creating a Tuple2
tpl2=(10,20,30,40,10,20,10) 
print("Created Tuple2 is ",tpl2)
print("Length : ", len(tpl2))
print("Min : ", min(tpl2))
print("Max : ", max(tpl2))
print("Count no. of 10's: ", tpl2.count(10))
print("Reverse Sort : ", sorted(tpl2,reverse=True))
print("")

'''
Set Theory
    Sets are used to store multiple items in a single variable.
    Set is one of 4 built-in data types in Python used to store collections of data
    A set is a collection which is both unordered and unindexed.
    Sets are written with curly brackets.
    Set items are unordered, unchangeable, and do not allow duplicate values.
'''
print( "---------------SET -----------------")
print( "")
s1={1,2,3,4,5,80,4,10,12,2}
s2=set()
s3={1,1.2,'aiktc'}
print(s1,s2,s3)
s1.add(60)
print(s1,s1.issuperset(s2))
print(s1.union(s3))

'''
Dictionary Theory

    Dictionaries are used to store data values in key:value pairs.
    A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
    Dictionaries are written with curly brackets, and have keys and values

'''
print("--------DICTIONARIES i.e. key:value pair------------")
print("")
d1={'Name':"Ahmed",'gender':"M",'age':20,'college':"AIKTC"} #create dictionary
print("print dictionary: ",d1)
print("")
print("-->Keys :",d1.keys())
print("-->Values :",d1.values())
print("-->Keys and values :",d1.items())
d1.update({'Name':"Sachin"})
print("-->Print updated dictionary: ",d1)

'''
Array Theory

    Python does not have built-in support for Arrays, but Python Lists can be used instead.
    Arrays are used to store multiple values in one single variable
    The length of an array is always one more than the highest array index.
    Python has a set of built-in methods that you can use on lists/arrays

'''
print("---------------ARRAYS -----------------")
print("")

#Create array with integer values
arr=array('i',[10,20,30,40,50]) 
print("The Array Elements are")

#i is element and arr in array name
for i in arr: 
    #Requires indentation
    print(i) 

print("length of array is",len(arr))
arr1=array('u',['a','b','c','d']) #Create array with character values
print("The Character Array Elements are")

#i is element and arr in array name
for i in arr1: 
    #Requires indentation
    print(i) 

'''
Conclusion: 

A data type constrains the values that an expression, such as a variable or a function, might take. This data type defines the operations that can be done on the data, the meaning of the data, and the way values of that type can be stored.
'''