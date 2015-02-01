
import string
from Tkinter import *
import cage
from collections import *
'''
This is v1 of the mouseRack application in Pyhton. It will contain an initialization class
that takes user input for rack name, and number of rows and columns. The program will then
initialize a GUI rack with the appropriate number of 'slots' for cages. Each slot will
be fillable with a cage Class. Cage classes will have a number of different info slots
and will have programable deadlines. They will change color (become 'hotter') as the due
date for the task approaches.

Persistance management:
'''
class Rack(Tk):


    def __init__(self, rack_frame,numRows, numCols):

        alpha = list(string.ascii_uppercase)

        self.numRows = int(numRows)
        self.numCols = int(numCols)


        def edit_cage(cage_name,frame):
            cage_name = cage.Cage(self,frame)
            Rack.view_edit(cage_name,frame)

        def add_cage():
            #I don't think I should do this as a nested function.
            #break it out ASAP
            def initializeCage():
                cageRow=int(rowInput.get())
                cageCol=colInput.get()
                cageName=idInput.get()

                #alphaDict converts a letter designation back to the appropriate
                #column number so tkinter grid can appropriately place the cage
                alphaDict = {}
                number = 0
                for letter in alpha:
                    alphaDict[letter] = number
                    number+=1



                activeFrame = label_frame_list[alphaDict[cageCol]][cageRow-1]
                activeEmptyLabel = label_list[alphaDict[cageCol]][cageRow-1]
                activeEmptyLabel.grid_forget()

                cageLabel= Button(activeFrame,text=cageName,command=lambda: edit_cage(cageName,rack_frame))

                cageLabel.grid()

                idInputLabel.grid_forget()
                idInput.grid_forget()
                rowInputLabel.grid_forget()
                rowInput.grid_forget()
                colInputLabel.grid_forget()
                colInput.grid_forget()
                addButton.grid_forget()



            idInputLabel=Label(rack_frame,text="Cage ID")
            idInput= Entry(rack_frame)
            idInputLabel.grid(row=1,column=self.numCols+1)
            idInput.grid(row=1,column=self.numCols+2)

            rowInputLabel=Label(rack_frame,text="Row")
            rowInput=Entry(rack_frame)
            rowInputLabel.grid(row=2,column=self.numCols+1)
            rowInput.grid(row=2,column=self.numCols+2)

            colInputLabel=Label(rack_frame,text="Column")
            colInput=Entry(rack_frame)
            colInputLabel.grid(row=3,column=self.numCols+1)
            colInput.grid(row=3,column=self.numCols+2)

            addButton = Button(rack_frame,text="Add",command=initializeCage)
            addButton.grid(row=4,column=self.numCols+2)


        #I am trying to put my labelframe and label objects into a list so I can access them easily
        #from elsewhere in the program
        #learn more about hte defaultdict class
        #TODO: LEARN more about defaultdict and understand how my two lists are being built here
        label_frame_list = defaultdict(list)
        label_list = defaultdict(list)
        for col in range(self.numCols):
            for r in range(self.numRows):
                label_frame_list[col].append(LabelFrame(rack_frame,text='{0}-{1}'.format(alpha[col],r+1)))
                l = label_frame_list[col][r]
                l.grid(row=r,column=col)


                label_list[col].append(Label(label_frame_list[col][r],text='empty'))
                label = label_list[col][r]
                label.grid()
        toolBar = Menu(rack_frame)
        toolBar.add_command(label="Add cage",command=add_cage)
        toolBar.add_command(label="Census")

        rack_frame.config(menu=toolBar)

    def view_edit(rack_frame):
        '''This command displays the cage contents on the sidebar
        the cage label is added as a label at the top of the field. Below
        this there is a yes/no button asking if the cage is a BU or not.
        Depending on the users answer different entry fields will be displayed.
        BU: male and female genotype, from, ET #, DOB (automatically generate
        breed date from this info using date/time package) ; set-up date,
        last litter (older litters will also be displayed but as labels, not
        as entry fields), NOTE: last litter will automatically generate a
        weaning TODO that the user can override, misc TODO field with date
        input

        For other cages the user will input the number of individuals and a
        series of fields will be generated as listed below
        Other cage: M/F, individual ID fields, genotype info for each ID input,
        TODO fields for each mouse
        '''


        #in order for buttons to have multiple functions when clicked
        #just write the command function to do everything you want it to.
        #duh.

        def bu_init():

            fields = ['Genotype','Ear tag #','from','DOB']
            row_counter = 2
            column_counter = numCols+1
            for field in fields:
                field_label = Label(rack_frame,text=field)
                field_entry = Entry(rack_frame)
                field_label.grid(row=2 , column=numCols+1)
                field_entry.grid(row=3 , column=numCols+1)
                column_counter+=1



        def other_init():
            pass

        cage_name_display = Label(rack_frame,text=self.cageName)
        cage_name_display.grid(row=1,column=numCols+1)


        BUbutton = Button(rack_frame, text='Breeding unit', command=bu_init)
        otherbutton = Button(rack_frame,text='Other cage', command=other_init)
        BUbutton.grid(row=2, column=numCols+1)
        otherbutton.grid(row=2, column=numCols+2)

        #toolBar = Menu(rack_frame)
        #toolBar.add_command(label="Add cage",command=add_cage)
        #toolBar.add_command(label="Census")

        #rack_frame.config(menu=toolBar)








'''VERSION #2
class Rack(Tk):


    def __init__(self, rack_frame,numRows, numCols):

        alpha = list(string.ascii_uppercase)

        self.numRows = int(numRows)
        self.numCols = int(numCols)


        def add_cage():
            #I don't think I should do this as a nested function.
            #break it out ASAP
            def initializeCage():
                cageRow=int(rowInput.get())
                cageCol=colInput.get()
                cageName=idInput.get()
                #alphaDict converts a letter designation back to the appropriate
                #column number so tkinter grid can appropriately place the cage
                alphaDict = {}
                number = 0
                for letter in alpha:
                    alphaDict[letter] = number
                    number+=1
                #How do I access labelframes from the original rack grid?
                cageLabel= Label(rack_frame,text=cageName)

                cageLabel.grid(row=cageRow-1,column=alphaDict[cageCol])



            idInputLabel=Label(rack_frame,text="Cage ID")
            idInput= Entry(rack_frame)
            idInputLabel.grid(row=1,column=self.numCols+1)
            idInput.grid(row=1,column=self.numCols+2)

            rowInputLabel=Label(rack_frame,text="Row")
            rowInput=Entry(rack_frame)
            rowInputLabel.grid(row=2,column=self.numCols+1)
            rowInput.grid(row=2,column=self.numCols+2)

            colInputLabel=Label(rack_frame,text="Column")
            colInput=Entry(rack_frame)
            colInputLabel.grid(row=3,column=self.numCols+1)
            colInput.grid(row=3,column=self.numCols+2)

            addButton = Button(rack_frame,text="Add",command=initializeCage)
            addButton.grid(row=4,column=self.numCols+2)




        for col in range(self.numCols):
            for r in range(self.numRows):

                L= LabelFrame(rack_frame,text='{0}-{1}'.format(alpha[col],r+1))
                L.grid(row=r,column=col)

                b= Label(L, text="Empty")
                b.grid()


        toolBar = Menu(rack_frame)
        toolBar.add_command(label="Add cage",command=add_cage)
        toolBar.add_command(label="Census")

        rack_frame.config(menu=toolBar)
'''










'''VERSION #1
class Rack(Tk):


    def __init__(self, rack_frame,numRows, numCols):
        alpha = list(string.ascii_uppercase)

        #rackFrame = Toplevel()
        #rackFrame.grid()

        self.numRows = int(numRows)
        self.numCols = int(numCols)

        #Going to use the labelframe widget type to populate the racks
        #slots = LabelFrame(rack_frame,padx=5, pady=5)
        #slots.grid()
        def add_cage():

            Cage()



        #right now I'm using this to generate the rightBar item below. This isn't a good solution

        for col in range(self.numCols):

            for r in range(self.numRows):
                L = LabelFrame(rack_frame,text='{0}-{1}'.format(alpha[col],r+1))
                L.grid(row=r,column=col)

                b= Button(L, text="Add cage",command=add_cage)
                b.grid()

        #TODO: implement this right action bar area that will host the cage entry and details section
        #rightBar = Frame(rack_frame,row=0, column=colCounter+1, rowspan=rowCounter+1)
        #rightBar.grid()


        #NOTE: instead of using text for the labels for my labelframes
        #containing the cages I should use labelwidget and make the widget
        #a drop down menu that allows the user to delete/change cages!








#root = Tk()

#rack_window = Toplevel()
#root.mainloop()
'''