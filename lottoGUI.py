from Tkinter import *
import tkMessageBox
import random

window = Tk()

greeting = Label(window, text="Hello and welcome\n to the fantastic\n lottery number generator!", font= "Courier 16 bold", fg="yellow", bg="light blue")\
    .pack(fill=X)
image = PhotoImage(file="../GUI/lottokugeln.gif")
main_image = Label(window, image=image, width=500, height=200, pady=10, bg="light blue").pack()
question = Label(window, text="Please enter how many numbers do you want!", font= "Courier 14 bold", fg="yellow", bg="light blue")\
    .pack(fill=X)

enter = Entry (window, font= "Courier 12 bold")
enter.pack(pady=20, padx= 30, ipady=5, ipadx=50)


def lotto_zahlen():
    lot_liste = []
    while True:
        if len(lot_liste) == int(enter.get()):

            break
        else:
            lot_nb = random.randint(1, 45)
            if lot_nb not in lot_liste:
                lot_liste.append(lot_nb)
    return tkMessageBox.showinfo("Lottery numbers:", lot_liste)


button = Button(window, text="Good Luck!", command=lotto_zahlen, font= "Courier 14 bold", fg="yellow", bg="light blue")\
    .pack(padx=10, pady=20, ipady=7, ipadx=50)

window.mainloop()


