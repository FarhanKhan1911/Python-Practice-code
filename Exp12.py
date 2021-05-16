'''
Exp 12: Program to demonstrate Data Series and DataFrame using Pandas.

Theory:
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data",
and "Python Data Analysis" and was created by Wes McKinney in 2008.
Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.

Key Features of Pandas:
Fast and efficient DataFrame object with default and customized indexing.
Tools for loading data into in-memory data objects from different file formats.
Data alignment and integrated handling of missing data.
Reshaping and pivoting of date sets.
Label-based slicing, indexing and subsetting of large data sets.
Columns from a data structure can be deleted or inserted.
Group by data for aggregation and transformations.
High performance merging and joining of data.
Time Series functionality.

@author: KHAN FARHAN NADEEM (19CO27)
'''

import pandas as pd 

#Series
'''
Series is a one-dimensional labeled array capable of holding data of any type
(integer, string, float, python objects, etc.). The axis labels are collectively called index.

A pandas Series can be created using the following constructor −
pandas.Series( data, index, dtype, copy)
data: data takes various forms like ndarray, list, constants
index: Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.
dtype: dtype is for data type. If None, data type will be inferred
copy: Copy data. Default False

A series can be created using various inputs like −
Array
Dict
Scalar value or constant

Create a Series from ndarray
If data is an ndarray, then index passed must be of the same length.
If no index is passed, then by default index will be range(n) where n is array length,
i.e., [0,1,2,3…. range(len(array))-1].
'''

# converting list to pandas series
s = pd.Series([
    [10,20,30,40,50],
    [20,40,30,20,20],
    [30,20,30,40,50],
    [30,40,10,50,10],
    [30,22,10,30,40],
    [30,40,10,50,10],
    ])
print('\nPandas Series \n')
print(s)
#some slicing, indexing, other features of Series

#slicing  

print('\nSeries Slicing\n')
print(s[:5])

#indexing
s = pd.Series([
    [10,20,30,40,50],
    [20,40,30,20,20],
    [30,20,30,40,50],
    [30,40,10,50,10],
    [30,22,10,30,40],
    [30,40,10,50,10],
    ],index=['i','ii','iii','iv','v','vi'])

print('\nIndexed series')
print(s)



#=========================#
#        Dataframe        #
#=========================#
'''
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
Pandas DataFrame is two-dimensional size-mutable,
potentially heterogeneous tabular data structure with labeled axes (rows and columns).
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
Pandas DataFrame consists of three principal components, the data, rows, and columns.

In the real world, a Pandas DataFrame will be created by loading the datasets from existing storage,
storage can be SQL Database, CSV file, and Excel file. Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc.
Features of DataFrame:
Potentially columns are of different types
Size – Mutable
Labeled axes (rows and columns)
Can Perform Arithmetic operations on rows and columns
Syntax -
#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
'''

player_list = [['M.S.Dhoni', 36, 75, 5428000], 
               ['A.B.D Villers', 38, 74, 3428000], 
               ['V.Kholi', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000], 
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]
  
# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df)

#some slicing, indexing, other features of Dataframes

#slicing

# slicing rows
df1 = df.iloc[0:4]
# data frame after slicing
print("\n Row wise slices data frame \n")
print(df1)

#slicing columns

df2=df.iloc[:,0:2]
print("\n Column wise slices data frame \n")
print(df2)

#indexing

student_list = [
    ['Khan zaki ur rahman',96,99,98,99,98,97],
    ['Khan Farhan Nadeem',97,98,97,98,99,99],
    ['Khan zikra',98,98,88,89,88,87],
    ['Khan Simi',96,90,98,98,88,97],
    ['Khan Muskan',96,99,98,99,98,97],
]
print('\nDate frame with indexing \n')
studentDf = pd.DataFrame(student_list,columns=['Name','Maths - 4','SBLC','OS','AOA','MP','DBMS'],index=['i','ii','iii','iv','v'])
print(studentDf)

#Sorting the data frame in Ascending order

player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kholi', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000], 
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]
  
# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
  
# Sorting by column 'Weight'
df.sort_values(by=['Weight'])


###########################################
#  Dataframe operations using csv dataset #
###########################################

#reading csv file
df = pd.read_csv('data.csv')
print('\n printing all data of data.csv file\n')
print(df.to_string()) 
#checking for missing values
print('\n Missing values \n')
print(df.isnull().sum())

# deleting the missing data
df = df.dropna()


# sorting the data.csv file data frame by calories
print('\n data frame after deleting null values and sorting by calories')
df1 = df.sort_values(by=['Calories'])
print(df1)

'''
Conclusion:
Pandas provide extremely streamlined forms of data representation.
This helps to analyze and understand data better. Simpler data representation facilitates better results for data science projects.
'''