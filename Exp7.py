'''
Exp 7: Implement a GUI Program using tkinter

Theory:

Tkinter 

Tkinter is the standard GUI library for Python. 
Python when combined with Tkinter provides a fast and easy way to create GUI applications. 
Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

*Creating a GUI application using Tkinter is an easy task. All you need to do is perform the following steps −

1]Import the Tkinter module.
2]Create the GUI application main window.
3]Add one or more of the above-mentioned widgets to the GUI application.
4]Enter the main event loop to take action against each event triggered by the user.

*Tkinter Widgets
Tkinter provides various controls, such as buttons, labels and text boxes used in a GUI application. These controls are commonly called widgets.
There are currently 15 types of widgets in Tkinter.

@author: KHAN FARHAN NADEEM (19CO27)
'''

from tkinter import *

class App:
    def __init__(self):
        self.root=Tk()
        self.root.title('GUI App')
        self.root.geometry('500x350')
        self.root.configure(background='light blue')
        #Labels are created
        self.rollno = Label(self.root, text="Roll No.", bg="light blue")
        self.name = Label(self.root, text="Name", bg="light blue")
        self.address = Label(self.root, text="Address", bg="light blue")
        self.mob = Label(self.root, text="Mobile", bg="light blue")
        #Labels are added on window
        self.rollno.grid(row=0,column=0)
        self.name.grid(row=1,column=0)
        self.address.grid(row=2,column=0)
        self.mob.grid(row=3,column=0)
        #Textfields are created
        self.rollnof = Entry(self.root)
        self.namef = Entry(self.root)
        self.addressf = Entry(self.root)
        self.mobf = Entry(self.root)
        #Textfields are added on window
        self.rollnof.grid(row=0,column=1,ipadx='100')
        self.namef.grid(row=1,column=1,ipadx='100')
        self.addressf.grid(row=2,column=1,ipadx='100')
        self.mobf.grid(row=3,column=1,ipadx='100')
        #Submit button created and added on window
        self.submit = Button(self.root, text="Submit", fg="Black", bg="light green", command=self.insert) 
        self.submit.grid(row=8, column=1,sticky=W+E)
        #Clear button created and added on window
        self.clear = Button(self.root, text="Clear",fg="Black", bg="light green", command=self.clearAll) 
        self.clear.grid(row=8, column=0,sticky=W+E)  
        self.root.mainloop()
    def insert(self):
        with open('student.csv','a') as file:
            rec=self.rollnof.get()+','+self.namef.get()+','+self.addressf.get()+','+self.mobf.get()+'\n'
            #rec=self.rollnof.get()+';'
            file.write(rec)

        
    def clearAll(self):
        self.rollnof.delete(0,'end')
        self.namef.delete(0,'end')
        self.addressf.delete(0,'end')
        self.mobf.delete(0,'end')

def main():
    myapp = App()

if __name__=='__main__':
    main()

'''
Conclusion

This framework provides Python users with a simple way to create GUI elements using the widgets found in the Tk toolkit. 
Tk widgets can be used to construct buttons, menus, data fields, etc. in a Python application.
'''    