#importing tkinter modules
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog
import analyze_gui

def main():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("750x600")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	# dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	# dnaInputLabel.place(x=20,y=160)

	#defining functions
	def homepage():
		window.destroy()
		analyze_gui.main()

	#defining buttons
	matching_percentage = Button(window, relief="solid",borderwidth=4, padx=40, text="Matching Percentage",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	matching_sequences = Button(window, relief="solid",borderwidth=4, padx=40, text="Most matching sequences",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	matching_nucleotides = Button(window, relief="solid",borderwidth=4, padx=40, text="Most matching nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	matching_virus = Button(window, relief="solid",borderwidth=4, padx=40, text="Most matching with virus",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=homepage)
	#openFileLabel = Button(window, relief="solid", borderwidth=4, padx=30, text="Open File",width=12,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=openFile)

	#defining input fields
	# dnaInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=30)
	# dnaInput.place(x=20,y=220)

	#displaying buttons
	matching_percentage.place(x=360,y=100)
	matching_sequences.place(x=360,y=190)
	matching_nucleotides.place(x=360,y=280)
	matching_virus.place(x=360,y=370)
	back.place(x=360,y=460)
	#openFileLabel.place(x=20,y=300)

	#running the program
	window.mainloop()
