#importing tkinter modules
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from main_imports import *
import main_gui

def main():

	#opening a window
	window = Tk()

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Central Dogma")

	# Setting the geometry i.e Dimensions
	window.geometry("750x500")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline().replace('\n',''))
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	def transcribeDNA():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		user_response = messagebox.showinfo(title='Transcription Result',message=f'The transcribed DNA: {transcribe(dna_seq)}')
		logOutput(f'The transcribed DNA: {transcribe(dna_seq)}')

	def openRNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		rna_file = open(file_path, 'r')
		rna_seq = check_RNA_validity(rna_file.readline().replace('\n',''))
		if not rna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		rnaSeqInput.insert(END, rna_seq)

	def translateRNA():
		rna_seq = check_RNA_validity(rnaSeqInput.get())
		if rna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not rna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		result = generate_polypeptides(rna_seq)
		if result:
			user_response = messagebox.showinfo(title='Translation Result',message=f'Translation Output: {result}')
			logOutput(f'Translation Output: {result}')
		else:
			user_response = messagebox.showinfo(title='Translation Result',message='Nothing to Translate!\nCheck your Sequence Start Codons')
			logOutput('Nothing to Translate!\nCheck your Sequence Start Codons')

	def automate_central_dogma():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		transc_dna_seq = transcribe(dna_seq)
		result = generate_polypeptides(transc_dna_seq)
		if result:
			user_response = messagebox.showinfo(title='Central Dogma Result',message=f'The Process Result: {result}')
			logOutput(f'The Process Result: {result}')
		else:
			user_response = messagebox.showinfo(title='Translation Result',message='Nothing to Translate!\nCheck your Sequence Start Codons')
			logOutput('Nothing to Translate!\nCheck your Sequence Start Codons')

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0,column=0)
	dnaInputLabel = Label(window, padx=20, pady=10, text="Your DNA Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=0,y=160)
	rnaInputLabel = Label(window, padx=20, pady=10, text="Your RNA Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	rnaInputLabel.place(x=0,y=330)

	#defining functions
	def homepage():
		window.destroy()
		main_gui.main()

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	button_transcription = Button(window, relief="solid",borderwidth=4, padx=40, pady=20, text="Transcribe DNA",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=transcribeDNA)
	button_translation = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Translate RNA",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=translateRNA)
	button_automation = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Automate Central Dogma",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=automate_central_dogma)
	back = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=homepage)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")
	button_openFileRNA = Button(window,borderwidth=0,image=fileImage,command=openRNAfile,bg="white")

	#displaying buttons
	button_transcription.place(x=360,y=100)
	button_translation.place(x=360,y=190)
	button_automation.place(x=360,y=280)
	back.place(x=360,y=370)
	button_openFileDNA.place(x=250,y=220)
	button_openFileRNA.place(x=250,y=390)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)
	rnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	rnaSeqInput.place(x=20,y=390)

	#running the program until the user clicks "X"
	window.mainloop()
