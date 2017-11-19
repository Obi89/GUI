from Tkinter import *
import tkMessageBox

window = Tk()
window2 = Tk()

img = PhotoImage(file="../GUI/menu.gif")
welcome = Label(window, text="Welcome to the MENU Programme!", font="Helvetica 18 bold").pack()
welcome2 = Label(window, image=img).pack()

dish_text = Label(window, text="Please enter a dish!", font="Helvetica 12 bold").pack()
dish_enter = Entry(window)
dish_enter.pack(padx= 30, ipady=5, ipadx=50)
price_text = Label(window, text="Please enter a price for the dish!", font="Helvetica 12 bold").pack()
price_enter = Entry(window)
price_enter.pack(padx= 30, ipady=5, ipadx=50)

menu = {}


def main():
    dish = dish_enter.get()
    price = float(price_enter.get())
    Label(window2, text="Dish: " + dish + "\nPrice: " + str(price)).pack()
    menu[dish] = price

def save():
    with open("menu.txt", "w+") as menu_file:
        menu_file.write("Menu:\n")
        for dish in menu:
         menu_file.write("- %s, %s EUR\n" %(dish, menu[dish]))


button = Button(window, text="Add menu!", command=main, font="Helvetica 14")
button.pack(pady=20)
button_save = Button(window2, text="Save!", command=save, font="Helvetica 12")
button_save.pack(pady=20)

window.mainloop()