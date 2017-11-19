from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from Tkinter import *
import tkMessageBox
import random

window = Tk()

greeting = Label(window, text="If you want some quotes on marriage,\n click the Button below!", font="Helvetica 18 bold italic", bg="white", fg="light blue")
greeting.pack(pady=20, fill=X)

def quotes():
    url = 'http://quotes.yourdictionary.com/theme/marriage/'
    html = urlopen(url).read()
    soup = BeautifulSoup(html)

    quotes = soup.findAll("p", attrs={"class": "quoteContent"})
    quotesnr = random.randint(0,20)
    tkMessageBox.showinfo("Some quote!", quotes[quotesnr].string)

button = Button(window, text="Show Me", command=quotes, font="Helvetica 16 bold italic", fg="white", bg="light blue")\
    .pack(pady=20)

window.mainloop()