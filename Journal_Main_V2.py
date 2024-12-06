#Journal main Attempt 2

import datetime
import tkinter
from tkinter import Button, Label, Frame

w_hori=1000
w_vert=600


'''
class window ():
    def __init__(self,x,y):
        #self.root= Tk()
        self.w_hori=y
        self.w_vert=x
#win=window("1000","600")
'''
root = tkinter.Tk("wi")
root.configure(height=w_vert,
              width=w_hori)
top = Frame(root,
            height=30,
            width=30,
            bg="red"
            )
print(top.winfo_parent())


    
class window():
    def __init__(self,master=None):
        
        self.master
