#-*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox

window = Tk()
logo = PhotoImage(file="../GUI/road.gif")
explanation = "Welcome to the unit converter!"
greeting_text = Label(window, text=explanation, fg = "light blue",
                      bg = "dark blue", font = "Helvetica 18 bold italic").pack(fill=X)
greeting_img = Label(window, image=logo, width=100, height=150).pack(fill=X, ipady=20)

Label(window, text="What do you want to convert?", fg = "blue", font = "Helvetica 10 bold italic").pack()
var1 = IntVar()
Checkbutton(window, text="km to miles", variable=var1,fg = "blue", font = "Helvetica 10 italic").pack()
var2 = IntVar()
Checkbutton(window, text="miles to km", variable=var2, fg = "blue", font = "Helvetica 10 italic").pack()


question_text = Label(window, text="Please enter a distance you like to convert!",fg = "blue", font = "Helvetica 10 bold italic").pack(fill=X)
question = Entry(window, bg="grey")
question.pack(padx= 30, ipady=5, ipadx=50)


def rechnen():
 try:
    if var1.get() == 1 and var2.get() == 0:
        data = float(question.get())
        miles = (data * 0.624)
        tkMessageBox.showinfo("Kilometers/Miles", str(data) + " km are " + str(miles) + " miles")
    elif var2.get() == 1 and var1.get() == 0:
        data = float(question.get())
        km = (data * 1.609)
        tkMessageBox.showinfo("Miles/Kilometers", str(data) + " miles are " + str(km) + " km")
 except ValueError:
     return


knopf = Button(window, text="Enter", command=rechnen, fg = "light blue", bg = "dark blue", font = "Helvetica 12 bold italic")
knopf.pack(padx=10, pady=20, ipady=7, ipadx=50)


window.mainloop()




