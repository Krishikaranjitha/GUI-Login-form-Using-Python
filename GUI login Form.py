from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Login")
root.geometry("300x300")

def login():
    username=Username.get()
    password=Password.get()
    
    if(username=="" and password==""):
        messagebox.showinfo("","Fields cannont be empty")
    elif(username=="Ranjitha" and password=="Krishika"):
        messagebox.showinfo("","Logged in Successfully")
    else:
        messagebox.showinfo("","Invalid")
        

global Username
global Password

Label(root,text="Username").place(x=25,y=20)
Label(root,text="Password").place(x=25,y=70)

Username=Entry(root,bd=5)
Username.place(x=100,y=20)

Password=Entry(root,bd=5)
Password.place(x=100,y=70)

Button(root,text="Login",command=login,height=1,width=10,bd=6).place(x=150,y=130)

root.mainloop()
