#I could have a button that asks if the cage is a BU/stock/plug etc.
#upon initialization

#TODO: display cage details upon mouseover of a particular cage!
#TODO: allow users to specify a slot as empty

from Tkinter import *

class Cage(Tk):



    def __init__(self,cageName,rack_frame):
        self.cageName = cageName




    '''
    #I am going to move the view_edit function to the rack file.
    def view_edit(self,rack_frame):
        This command displays the cage contents on the sidebar
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
        '''









'''Version #1
class Cage(Tk):



    def __init__(self):

        cageFrame = Toplevel()
        cageFrame.grid()
        cageFrame.title('Enter cage ID')

        self.cageIdLabel = Label(cageFrame, text='Please enter cage ID')
        self.cageIdLabel.grid(row=0,column=1)
        self.cageId = Entry(cageFrame)
        self.cageId.grid(row=0, column=2)



    def view(self):
        pass



'''