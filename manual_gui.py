#importing modules, PIL is the module that allows us to use images in .jpg, .jpeg, and .png, which are most popular
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from tkinter import messagebox
import main_gui

def main():
	global MainLabel
	global rightBtn
	global leftBtn

	#initializing the program and giving the window some properties
	window = Tk()
	window.title("PySequence - Version 1.0 / Manual")
	window.geometry("900x630")
	window.resizable(0,0)
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#pySequence logo
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0,column=0)

	#defining the images
	img0 = ImageTk.PhotoImage(Image.open("Images/pairings.png"))
	img1 = ImageTk.PhotoImage(Image.open("Images/centralDogma.png"))
	img2 = ImageTk.PhotoImage(Image.open("Images/polypeptide.png"))
	img3 = ImageTk.PhotoImage(Image.open("Images/translation.png"))

	#putting images in a list
	ImageList = [img0,img1,img2,img3]

	#passing the first image to a label, and displaying the label on the screen
	MainLabel = Label(image=img0)
	MainLabel.grid(row=2,column=2,columnspan=3)

	#defining the function that changes images
	def swipeRight(imageNum):
		global MainLabel
		global rightBtn
		global leftBtn
		MainLabel.grid_forget()
		MainLabel = Label(image=ImageList[imageNum])
		rightBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, command=lambda: swipeRight(imageNum+1), text="Swipe Right")
		leftBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, command=lambda: swipeLeft(imageNum-1), text="Swipe Left")

		if imageNum == 3:
			rightBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, text="Swipe Right",state=DISABLED)

		leftBtn.grid(row=3,column=2)
		rightBtn.grid(row=3,column=4)
		MainLabel.grid(row=2,column=2,columnspan=3)

	def swipeLeft(imageNum):
		global MainLabel
		global leftBtn
		global rightBtn
		MainLabel.grid_forget()
		MainLabel = Label(image=ImageList[imageNum])
		rightBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, command=lambda: swipeRight(imageNum+1), text="Swipe Right")
		leftBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, command=lambda: swipeLeft(imageNum-1), text="Swipe Left")

		if imageNum == 0:
			leftBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, text="Swipe Left",state=DISABLED)

		leftBtn.grid(row=3,column=2)
		rightBtn.grid(row=3,column=4)
		MainLabel.grid(row=2,column=2,columnspan=3)

	def homepage():
		window.destroy()
		main_gui.main()


	#defining right and left buttons and exit button
	leftBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, command= swipeLeft, text="Swipe Left", state=DISABLED)
	rightBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, command= lambda: swipeRight(1), text="Swipe Right")
	BackProgramBtn = Button(window, pady=5, font="Helvetica 16 bold italic", fg="dark blue", bg="dark cyan", relief="solid", width=10, height=2, text="Back", command=homepage)



	#displaying right and left buttons and exit button
	leftBtn.grid(row=3,column=2)
	rightBtn.grid(row=3,column=4)
	BackProgramBtn.grid(row=3,column=3)


	#running the program
	window.mainloop()
