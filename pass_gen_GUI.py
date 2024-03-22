from tkinter import * 
import string
import random
import pyperclip


calc = ""

def generator():
    alpha = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    number = "1234567890"
    symbol="!@#$%^&*()-_=+,.';:<>?{}[]"
    type  = alpha + number + symbol
    password_length = int(lengthbox.get())
    password = random.sample(type,password_length)
    passbox.insert("0.0",password)
    
def clear():
    global calc
    calc = ""
    passbox.delete(1.0,"end")

def copy():
    copy_password = passbox.get("1.0", 'end-1c')
    pyperclip.copy(copy_password)



box = Tk()
box.config(bg= "silver")

box.title("Password Generator")
box.geometry("300x350")

passwordLabel=Label(box, text='Password Generator' , font = ("Arial", 20, "bold") , background="silver")
passwordLabel.grid(pady = 5)

lengthLabel=Label(box, text='Password Length' , font = ("Arial", 15, "bold") , background="silver")
lengthLabel.grid(pady = 2)

lengthbox = Spinbox(box, from_=5, to_=16, width = 5, font = ("Arial, 20") )
lengthbox.grid(pady = 5)

genbutton = Button(box, text= "Generate", font = ("Arial", 15) , background="red" , command = generator , )
genbutton.grid(pady = 5)

delbutton = Button(box, text = "Clear" , font= ("Arial" , 15) ,background = "red" , command = clear)
delbutton.grid(pady = 5)


passbox = Text(box, height = 2 , width = 21, font = ("Times New Roman", 20), background="black" ,fg = "white")
passbox.grid(columnspan= 5, pady = 5)

copybutton = Button(box, text= "Copy", font = ("Arial", 10,  "bold") , width = 12 , background="red" , command = copy)
copybutton.grid(pady = 5)


box.mainloop()










