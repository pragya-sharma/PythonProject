from tkinter import *


def getVals():
    print(f"userName : {userValue.get()}")
    print(f"userPassword : {passValue.get()}")


root = Tk()
root.geometry("555x456")
root.title("My First Login Page")

userName = Label(root, text="UserName ")
password = Label(root, text="Password ")
userName.grid()
password.grid(row=1)
userValue = StringVar()
passValue = StringVar()
userEntry = Entry(root, textvariable=userValue)
passEntry = Entry(root, textvariable=passValue)
userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

Button(text="submit", command=getVals).grid()
root.mainloop()
