#Journal Documenter
#Filename = Date + File name inputted.

from tkinter import *
from tkinter import Button, Label, messagebox
import datetime
import os

directory="Add Folder Directory Here" #Add folder directory Here.

w_height=500 #Window Height.
w_width=1000 #Window Width.

#Window functions. Possibly replacable by relx & rely (relative x?, relative y?)
def w_percentage_W(percentage):
    return w_width/100*percentage
def w_percentage_H(percentage):
    return w_height/100*percentage

#Frame functions. Possibly replacable by relx & rely 
def f_perc_W(frame_x, perc):
    return frame_x/100*perc
def f_perc_H(frame_y, perc):
    return frame_y/100*perc

#Breaks downa and stores Day, Month, Year values of Today.
class filename():
    def __init__(self, master=None):
        self.day = (datetime.date.fromisoformat(str(datetime.date.today()))) #Gets dates
        self.day = str(self.day).split("-") #splits YY,MM,DD
        self.year, self.month, self.day = self.day #sets YY,MM,DD into their variables.

    def printdate(self):
        print(self.day)
        print(self.month)
        print(self.year)
        
fdtn = filename()
fdtn.printdate()

#WINDOW
win=Tk()
win.geometry(f"{w_width}x{w_height}")
win.configure(bg='grey')
win.title("window test")
win.resizable(height=False,width=False)#Window is not resizable.

#Low FRAME

l_frame = Frame(win,
               bg='green',
               height= w_percentage_H(20),
               width= w_percentage_W(100))
l_frame.place(y=w_percentage_H(80),x=w_percentage_W(0))

#TOP FRAME

t_frame= Frame(win,
               bg='blue',
               height=w_percentage_H(20),
               width=w_percentage_W(100))
t_frame.place(y=w_percentage_H(0),x=w_percentage_W(0)) #0,0

    #Heading
t_lab=Label(t_frame,
          bg="black",
          fg='white',
          font='80',
          text="Write Document")
t_lab.place(relx=0.5,rely=0, anchor="n")


    #Date Time Name Generation
t_Ent= Entry(t_frame,
             bg='grey',
             font="40",
             width=10)
             # Adds default text.
t_Ent.insert(0,str(fdtn.day)+"_")
t_Ent.insert(0,str(fdtn.month)+"-")
t_Ent.insert(0,str(fdtn.year)+"-")
t_Ent.place(relx=0.05, rely=0.8, anchor="sw") #relx/rely = percentage placement. 1=100%,0=0%

    #Date Time Name Input
t_Ent2 = Entry(t_frame,
               bg="white",
               font="40")
t_Ent2.insert(0, "<Add File Name Here>")
t_Ent2.place(relx=0.15, rely=0.8, anchor="sw")

t_Ent2_Error = Label(t_frame,
                   text="",
                   font="40" "red")
t_Ent2_Error.place(relx=0.15,rely=0.9,anchor="w")

#CENTRE FRAME
centre = Frame(win,
               bg='red',
               height=w_percentage_H(60),
               width=w_percentage_W(100))
centre.place(y=w_percentage_H(20),x=w_percentage_W(0))

#Centre Text
c_text= Text(centre,
             bg='white',
             yscrollcommand=True #Allows scrolling up and down.
             )
c_text.place(relx=0.5,rely=0.5,anchor="center",relheight=0.9,relwidth=0.9)

lab = Label(l_frame,
             font=('',48),
             text="text")

#Button Functions.

def saveFile(): #Saves file contents as the name inputted.
    global c_text #Paragraphs
    global t_Ent #Date
    global t_Ent2 #Name
    global t_Ent2_Error
    filename = (t_Ent.get()+t_Ent2.get()) #Creates file name

    #Changes file content.
    if os.path.exists(directory+f"\{filename}.txt") == True:
        
        if messagebox.askyesno(title="Save?",message="Any changes made will be irreversible. Continue?")==True: #Only saves once player has agreed with the message.
            try:
                with open(f"{filename}.txt", "w+") as f:
                    f.write(c_text.get(0.0,END))
            except:
                t_Ent2_Error.configure(text="Failed Save") #Informs user of failed save
            finally:
                print("Exists")
                time_pnt = datetime.datetime.now()
                print(time_pnt)
    #If its a new file, creates new file.
    else:
        try:
            with open(f"{filename}.txt", "x") as f: #Creates a file with the inputted name.
                f.write(c_text.get(0.0,END))#Saves Contents from line and row 0.0 (Dont know why it uses a "." instead of "," or parenthesis.)
                t_Ent2_Error.configure(text="Saved")#Informs user of save
        except:
            t_Ent2_Error.configure(text="Failed Save") #Informs user of failed save
        finally:
            time_pnt = datetime.datetime.now()
            print(time_pnt)
def saveFileAs():
    print("SaveFileAs")


def openfile():
    global c_text #Paragraphs
    global t_Ent #Date
    global t_Ent2 #Name
    filename = (t_Ent.get()+t_Ent2.get())
    cont_as_op = None
    unsaved_cont = False
    if (len(c_text.get(0.0,END))-1) >= 1: #Checks whether there is any existing work.
        unsaved_cont = True
    
    if unsaved_cont==True:
        if messagebox.askyesno(title="Open new File?", message="Opening a new file will remove any unsaved work. Continue?") == True: #If work exists and user wants to open folder, then open new file.
            try:
                #File found
                if os.path.exists(directory+f"\{filename}.txt") == True:
                    c_text.delete(0.0,END) #Deletes previous work before opening new file.
                    print("EXISTS")
                    with open(f"{filename}.txt", "r") as f:
                        c_text.insert(0.0, f.read())
                else: #NEEDS FALSE OUTPUT TO TRIGGER EXCEPT.
                    print("False")
                    raise ValueError
            except: #File not found
                print("Error")
                messagebox.showerror(title="Error",message="File not found") #messagebox doesnt need a parent.
    else: #Existing work = False
        try:
            #File found
            if os.path.exists(directory+f"\{filename}.txt") == True:
                c_text.delete(0.0,END) #Deletes previous work before opening new file.
                print("EXISTS")
                with open(f"{filename}.txt", "r") as f:
                    c_text.insert(0.0, f.read())
            else: #NEEDS FALSE OUTPUT TO TRIGGER EXCEPT.
                print("False")
                raise ValueError
        except: #File not found
            print("Error")
            messagebox.showerror(title="Error",message="File not found") #messagebox doesnt need a parent.

def clear():
    global c_text
    print(c_text.delete(0.0,END))#Deletes c_text Contents.
    

#Buttons

l_btn1 = Button(l_frame,
                text="Clear",
                bg="red",
                command=clear)
l_btn1.place(relx=0.05, rely=0.5, anchor="sw")

    #Save Buttons
        #btn1 - Save File.
l_Btn = Button(t_frame,
               text="Save",
               command=saveFile)

l_Btn.place(relx=0.4, rely=0.8, anchor="sw")
'''
        #btn2 - Save AS - Not functional.
l_Btn2=Button(t_frame,
             text="Save As",
             command=saveFileAs)
l_Btn2.place(relx=0.45,rely=0.8, anchor="sw")
'''
        #btn3 - Open File.
l_Btn3=Button(t_frame,
              text="Open",
              command=openfile)
l_Btn3.place(relx=0.55, rely=0.8, anchor="sw")
