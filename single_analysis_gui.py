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
	window.geometry("750x750")

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
	count = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	complement = Button(window, relief="solid",borderwidth=4, padx=40, text="Complementary Strand",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	gcContent = Button(window, relief="solid",borderwidth=4, padx=40, text="G-C Content",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	palindrome = Button(window, relief="solid",borderwidth=4, padx=40, text="Palindrome?",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	ligate = Button(window, relief="solid",borderwidth=4, padx=40, text="Ligate a Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	segmentSearch = Button(window, relief="solid",borderwidth=4, padx=40, text="Search for Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	segmentCount = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	reverseComplement = Button(window, relief="solid",borderwidth=4, padx=40, text="Reverse Complementary",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	reverseTranscriptase = Button(window, relief="solid", borderwidth=4, padx=40, text="Reverse Transcriptase",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=homepage)
	#openFileLabel = Button(window, relief="solid", borderwidth=4, padx=30, text="Open File",width=12,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=openFile)

	#defining input fields and file navigation
	# dnaInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=30)
	# dnaInput.place(x=20,y=220)

	#displaying buttons
	count.place(x=360,y=100)
	complement.place(x=360,y=160)
	gcContent.place(x=360,y=220)
	palindrome.place(x=360,y=280)
	ligate.place(x=360,y=340)
	segmentSearch.place(x=360,y=400)
	segmentCount.place(x=360,y=460)
	reverseComplement.place(x=360,y=520)
	reverseTranscriptase.place(x=360,y=580)
	back.place(x=360,y=640)
	#openFileLabel.place(x=20,y=300)

	#running the program
	window.mainloop()
