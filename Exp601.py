'''
Experiment 6.1: Python program to append data to existing file and then display the entire file.

Theory:

File Handling
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

*There are four different methods (modes) for opening a file:

1]"r" - Read - Default value. Opens a file for reading, error if the file does not exist
2]"a" - Append - Opens a file for appending, creates the file if it does not exist
3]"w" - Write - Opens a file for writing, creates the file if it does not exist
4]"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

1]"t" - Text - Default value. Text mode
2]"b" - Binary - Binary mode (e.g. images)

1]Open a File
To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:
If the file is located in a different location, you will have to specify the file path

3]Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return
You can return one line by using the readline() method
By calling readline() two times, you can read the two first lines
By looping through the lines of the file, you can read the whole file, line by line

4]Close Files
It is a good practice to always close the file when you are done with it.

5]Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

6]Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

7]Delete a File
To delete a file, you must import the OS module, and run its os.remove() function
To delete an entire folder, use the os.rmdir() method

@author: KHAN FARHAN NADEEM (19CO27)
'''

filename = input("Enter the file name : ")

f = open(filename,'a')
data = input(f"Enter the data to append at the end of file {filename} : \n")
f.write(data)

f = open(filename,'r')
print(f.read())