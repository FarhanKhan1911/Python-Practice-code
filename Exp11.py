'''
Exp 11: Program to demonstrate use of NumPy: Array objects.

Theory:
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
NumPy stands for Numerical Python.

In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
These are the most common and basic arrays.
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.
These are often used to represent matrix or 2nd order tensors.

arange() is an inbuilt numpy function that returns an ndarray object containing evenly spaced values within a defined interval.
linspace() function returns number spaces evenly w.r.t interval.
Similar to numpy.arange() function but instead of step it uses sample number.
logspace() function returns number spaces evenly w.r.t interval on a log scale.
zeros() function returns a new array of given shape and type, with zeros.
ones() function returns a new array of given shape and type, with ones.
empty() is used to create an array without initializing the entries of given shape and type.
identity() Return a identity matrix i.e. a square matrix with ones on the main diagonal.

Slicing:
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1

@author: KHAN FARHAN NADEEM (19CO27)
'''

import numpy as np
#############################
#    creating numpy arrays  #
#############################
#########################################
# create 1D arrays using array function #
#########################################
arr1d = np.array([1,2])

#######################################################
# create 2D arrays using array function of type float #
#######################################################
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)


######################################
# create array using arange function #
######################################
arr_ar = np.arange(1,100,9)

########################################
# create array using linspace function #
########################################
arr_lp = np.linspace(10,11,10)

########################################
# create array using logspace function #
########################################
arr_logp = np.logspace(10,15,10)

########################################
# create array using various functions #
########################################
arr_zeros = np.zeros((2,3))
arr_ones = np.ones((3,2))
arr_empty = np.empty((2,4))
arr_identity = np.identity(3)

##############################
## accessing array elements ##
##############################
print('\n arr1d =',arr1d)
print('\n arr2d =')

for row in arr2d:
    print(row)

print('\narr_ar =',arr_ar)
print('\narr_lp =',arr_lp,' having size of',arr_lp.size)
print('\narr_logp =',arr_logp,' having size of',arr_logp.size)
print('\narr_zeros =\n',arr_zeros)
print('\narr_ones =\n',arr_ones)
print('\narr_empty =\n',arr_empty)
print('\narr_identity =\n',arr_identity)

###################################
###  performing array operations ##
###################################
print('\nPerforming Array Operations:')
print('Addition of 2D arrays\n',arr2d + arr_identity)
print('Substraction of 2D arrays\n',arr2d - arr_identity)
print('Multiplication of 2D arrays\n',arr2d * arr_identity)
print('Matrix Multiplication of 2D arrays\n',arr2d @ arr_identity)
print('Transpose of 2D arrays\n',arr2d.transpose())

###############################
# performing slice operations #
###############################
print('Elements of Second Row and First 2 Columns',arr2d[1,:2])
print('Elements of Last Row and Second Column onwards',arr2d[-1,1:])
print(arr2d[arr1d])

################################
# performing reshape on arrays #
################################

##################################
# reshaping 1D array to 2D array #
##################################
newarr = arr1d.reshape(1,2)
print('reshaped array : ',newarr)

'''
Conclusion:
NumPy is a fundamental package for scientific computation & mathematical operations in python.
NumPy is way more powerful than Lists.
'''