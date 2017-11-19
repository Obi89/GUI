from Tkinter import *
import tkMessageBox
import random

secret = random.randint(0,100)

window = Tk()
img = PhotoImage(file="numbers.gif")
greeting = Label(window, text="Guess the secret number!", fg="lawn green", bg="black", font="bold 16")
greeting.pack(pady=10)
main_img = Label(window, image=img, width=160, height=100)
main_img.pack()
eingabefeld = Entry(window, font="15")
eingabefeld.pack(pady=10)

def geklicked():
    try:
        eingabe = int(eingabefeld.get())
    except ValueError:
        return
    if eingabe == secret:
        tkMessageBox.showinfo("Yeah!", "The answer is Correct!")
    elif eingabe > secret:
        tkMessageBox.showerror("False!", "Your guess is not correct... try something smaller")
    else:
        tkMessageBox.showerror("False!", "Your guess is not correct... try something bigger")


knopf = Button(window, text="Guess!", command=geklicked, bg="lawn green", font="bold")
knopf.pack(pady=10, ipadx=40)


print "for dem erstellen"
window.mainloop()
print "nach dem schliessen"



