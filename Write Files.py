#Working with Files
from datetime import date
import os

'''
with open("test.txt", w) as f:
    f.read()
'''

#Creates File

'''
file = open("test", "w")
file.write("hello world") #Adds Text.
cont = file.read()
print(cont)
file.close()
'''

#Creates the file Name, using [DATE] + [USER_INPUT]
today = date.today()
print(today)
name=str(input("File Name: "))
title=(str(f"{today}"+"_"+f"{name}.txt")) # character : cant be used.
print(title)

#Create the File within the same file location as the Python File.

try:
    with open(f"{title}", "xt", encoding="utf-8") as f: #Opens. Wt(write to needs a target. However xt can be used to replace.)
        text = (input("Input text: ")) #File Content
        f.write(text)
        #print(input("input"), (f"{title}"))

except:
    with open(f"{title}", "wt", encoding="utf-8") as f: #Only write when mode is wt.
        text = (input("Input text: "))#File Content
        f.write(text)
    
    with open(f"{title}", "rt", newline='') as f: #Only read in rt.
        cont=f.read()
        print(cont)

    # OR THIS METHOD CAN BE USED!!!!! 
finally:
    if not os.path.exists(title): #value opposit due to NOT.
        print("Does not exist")
    else:
        print("Exists")
