'''
Write a program to perform a below given operation on Students marklist in SQLDB with GUI.
1.Create
2.Update
3.Read
4.Delete
'''

import pymysql
from tkinter import *

root = Tk()
root.title("Mark List")
root.geometry("500x250")

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Reg.No").grid(row=0, column=3)
Label(root, text="DOB").grid(row=1, column=0)
Label(root, text="Ph.No").grid(row=2, column=0)
Label(root, text="Email ID").grid(row=3, column=0)
Label(root, text="Subject", bg="grey").grid(row=4, column=1)
Label(root, text="Marks", bg="grey").grid(row=4, column=2)
Label(root, text="Science").grid(row=5, column=1)
Label(root, text="Maths").grid(row=6, column=1)
Label(root, text="GK").grid(row=7, column=1)
Label(root, text="English").grid(row=8, column=1)
Label(root, text="Hindi").grid(row=9, column=1)
Label(root, text="Total").grid(row=9, column=3)
Label(root, text="Average").grid(row=10, column=3)

name = Entry(root)
reg_no = Entry(root)
dob = Entry(root)
email = Entry(root)
ph_no = Entry(root)
mark1 = Entry(root)
mark2 = Entry(root)
mark3 = Entry(root)
mark4 = Entry(root)
mark5 = Entry(root)

name.grid(row=0, column=1)
reg_no.grid(row=0, column=4)
dob.grid(row=1, column=1)
email.grid(row=3, column=1)
ph_no.grid(row=2, column=1)
mark1.grid(row=5, column=2)
mark2.grid(row=6, column=2)
mark3.grid(row=7, column=2)
mark4.grid(row=8, column=2)
mark5.grid(row=9, column=2)

def submit():
    db = pymysql.connect(host="localhost",user="root",password="Shamala",database="class")
    cursor = db.cursor()
    
    global tot
    global avg

    Name = name.get()
    Reg_No = reg_no.get()
    DOB = dob.get()
    Email = email.get()
    Ph_No = ph_no.get()
    Science = float(mark1.get())
    Maths = float(mark2.get())
    GK = float(mark3.get())
    English = float(mark4.get())
    Hindi = float(mark5.get())

    total = Science+Maths+GK+English+Hindi
    average = total/5

    tot = Label(root, text=str(total))
    tot.grid(row=9, column=4)

    avg = Label(root, text=str(average))
    avg.grid(row=10, column=4)

    ins = "INSERT INTO mark_list(Name, Reg_No, DOB, Email, Ph_No, Science, Maths, GK, English, Hindi, total, average) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (Name,Reg_No,DOB,Email,Ph_No,int(Science),int(Maths),int(GK),int(English),int(Hindi),float(total),float(average))
    cursor.execute(ins,values)
    db.commit()

    name.delete(0, END)
    reg_no.delete(0, END)
    dob.delete(0, END)
    email.delete(0, END)
    ph_no.delete(0, END)
    mark1.delete(0, END)
    mark2.delete(0, END)
    mark3.delete(0, END)
    mark4.delete(0, END)
    mark5.delete(0, END)
    tot.destroy()
    avg.destroy()

Button(root,text="Submit",bg="green",command=submit).grid(row=10,column=1)


root.mainloop()

    
    
    
