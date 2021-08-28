#importing tkinter modules
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

#opening a window
window = Tk()

#naming the title of the program
window.title("PySequence - Version 1.0 / Analyze")

# Setting the geometry i.e Dimensions
window.geometry("750x500")

#disabling maximize and minimize buttons
window.resizable(0,0)

#changing background color
window.configure(background="white")

#font styling
nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

#defining labels
name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)

#defining functions
def homepage():
	window.destroy()
	import main_gui

def singleStrandPage():
	window.destroy()
	import single_analysis_gui

def multiStrandPage():
	window.destroy()
	import multi_analysis_gui

#defining buttons
singleStrand = Button(window, relief="solid",borderwidth=4, padx=40, pady=20, text="Single Strand Analysis",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=singleStrandPage)
multiStrand = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Multi Strand Analysis",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=multiStrandPage)
back = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=homepage)

#displaying buttons
singleStrand.place(x=360,y=100)
multiStrand.place(x=360,y=190)
back.place(x=360,y=280)

#running the program
window.mainloop()