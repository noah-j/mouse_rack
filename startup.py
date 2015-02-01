

import string
from Tkinter import *
from rack import *

class Startup(object):

    def __init__(self, master):
        frame = Frame(master)

        frame.grid()


        self.rowLabel = Label(master, text="# of rows")
        self.rowLabel.grid(row=0, column=1)
        self.rowPicker= Entry(master)
        self.rowPicker.grid(row=0,column=2)

        self.colLabel = Label(master, text="# of columns")
        self.colLabel.grid(row=1, column=1)
        self.colPicker = Entry(master)
        self.colPicker.grid(row=1, column=2)

        self.nameLabel= Label(master, text="Name of rack")
        self.nameLabel.grid(row=2, column=1)
        self.rackName  = Entry(master)
        self.rackName.grid(row=2, column=2)



        def launch():

            name = self.rackName.get()
            rows = self.rowPicker.get()
            cols = self.colPicker.get()
            rackFrame = Toplevel()
            rackFrame.title('{}'.format(self.rackName.get()))
            rackFrame.grid()

            try:
                #I don't actually want to kill all the original widgets here
                #I want the new Rack instance to launch in its own seperate window

                #self.rowLabel.destroy()
                #self.colLabel.destroy()
                #self.nameLabel.destroy()
                #self.rowPicker.destroy()
                #self.colPicker.destroy()
                #self.rackName.destroy()
                #self.launchButton.destroy()
                ###I got it. The issue was not specifying the frame in the rack method
                ### __init__ at the Label button
                name = Rack(rackFrame,rows, cols)

            except ValueError:
                #This should be made into a pop up window warning about
                #using the correct input types
                exceptionPrompt=Label(rackFrame,text='please enter integers for row and column numbers  ')

        nGet = self.rackName.get()
        rGet = self.rowPicker.get()
        cGet = self.colPicker.get()
        self.launchButton = Button(master, text="Create rack", command=launch)
        self.launchButton.grid(row=3)







root= Tk()
starter = Startup(root)
root.mainloop()









































#version 1
'''
class Startup:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        l1 = Label(root,text='MouseRack v1')
        l1.pack()

        self.rowPicker= Listbox(master, selectmode=SINGLE)
        self.rowPicker.pack()

        self.colPicker = Listbox(master, selectmode=SINGLE)
        self.colPicker.pack()

        for item in range(10):
            self.rowPicker.insert(END, item)
            self.colPicker.insert(END, item)


    def selection(self,master):

        numRows = self.rowPicker.curselection()
        numCols = self.colPicker.curselection()


        rackName  = raw_input('Please enter rack ID')


        self.choiceButton = Button(master, text='Initialize', command=rackname.Rack(numRows,numCols))


root= Tk()
starter = Startup(root)
root.mainloop()
'''