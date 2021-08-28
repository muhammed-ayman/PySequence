#importing tkinter modules
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog
import analyze_gui
from main_imports import *


def reverse_complement_sub():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

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
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()


	def reverse_complement_local():
		rna_seq = check_RNA_validity(dnaSeqInput.get())
		if rna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not rna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output = reverse_complement(rna_seq)
		user_response = messagebox.showinfo(title='Reverse Complementary Strad',message=f'The reverse of the complement of your enetred strand is > {feature_output}')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openRNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		rna_file = open(file_path, 'r')
		rna_seq = check_RNA_validity(rna_file.readline())
		if not rna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, rna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")


	#defining buttons
	complementbtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Reverse Complement",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=reverse_complement_local)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)

	button_openFileRNA = Button(window,borderwidth=0,image=fileImage,command=openRNAfile,bg="white")

	#displaying buttons
	button_openFileRNA.place(x=250,y=220)
	complementbtn.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()


def count_segment_sub():

	#opening a window
	window = Tk()

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("800x700")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	dnaInputLabel1 = Label(window, padx=20, pady=10, text="Enter the DNA Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel1.place(x=20,y=160)
	dnaInputLabel2 = Label(window, padx=20, pady=10, text="Enter the segment you want to count",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel2.place(x=20,y=260)

	#defining functions
	def back():
		window.destroy()
		main()

	def count_segment_local():
		dna_seq = check_DNA_validity(dnaSeqInput1.get())
		dna_segment = check_DNA_validity(dnaSeqInput2.get())
		if dna_seq == '' or dna_segment == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq or not dna_segment:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return

		feature_output = STPs(dna_seq, dna_segment)
		if feature_output != 0:
			user_response = messagebox.showinfo(title='Does Segment Exist?',message=f'Your segment occurs {feature_output} times!')
		else:
			user_response = messagebox.showinfo(title='Does Segment Exist?',message=f'Your segment doesn\'t occur in the strand')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile1():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput1.insert(END, dna_seq)

	def openDNAfile2():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput2.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	searchSegmentBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=count_segment_local)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA1 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile1,bg="white")
	button_openFileDNA2 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile2,bg="white")

	#displaying buttons
	button_openFileDNA1.place(x=250,y=220)
	button_openFileDNA2.place(x=250,y=320)
	searchSegmentBtn.place(x=360,y=540)
	back.place(x=360,y=600)

	#defining input fields
	dnaSeqInput1 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput1.place(x=20,y=220)
	dnaSeqInput2 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput2.place(x=20,y=320)

	window.mainloop()

def search_segment_sub():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("800x700")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	dnaInputLabel1 = Label(window, padx=20, pady=10, text="Enter the DNA Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel1.place(x=20,y=160)
	dnaInputLabel2 = Label(window, padx=20, pady=10, text="Enter the segment you want to search for",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel2.place(x=20,y=260)

	#defining functions
	def back():
		window.destroy()
		main()

	def search_segment_local():
		dna_seq = check_DNA_validity(dnaSeqInput1.get())
		dna_segment = check_DNA_validity(dnaSeqInput2.get())
		if dna_seq == '' or dna_segment == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq or not dna_segment:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return

		feature_output = feature_output = ' does ' if restriction_enzyme(dna_seq , dna_segment) else ' does NOT '
		user_response = messagebox.showinfo(title='Does Segment Exist?',message=f'Your segment{feature_output}exist in the strand!')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile1():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput1.insert(END, dna_seq)

	def openDNAfile2():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput2.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	searchSegmentBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Ligate",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=search_segment_local)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA1 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile1,bg="white")
	button_openFileDNA2 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile2,bg="white")

	#displaying buttons
	button_openFileDNA1.place(x=250,y=220)
	button_openFileDNA2.place(x=250,y=320)
	searchSegmentBtn.place(x=360,y=540)
	back.place(x=360,y=600)

	#defining input fields
	dnaSeqInput1 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput1.place(x=20,y=220)
	dnaSeqInput2 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput2.place(x=20,y=320)

	window.mainloop()

def ligate_sub():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

	# Setting the geometry i.e Dimensions
	window.geometry("800x700")

	#disabling maximize and minimize buttons
	window.resizable(0,0)

	#changing background color
	window.configure(background="white")

	#font styling
	nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

	#defining labels
	name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white").grid(row=0, column=0)
	dnaInputLabel1 = Label(window, padx=20, pady=10, text="Enter the DNA Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel1.place(x=20,y=160)
	dnaInputLabel2 = Label(window, padx=20, pady=10, text="Enter the segment you want to ligate to the original sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel2.place(x=20,y=260)
	dnaIndex = Label(window, padx=20, pady=10, text="Enter the nucleotide index after which you want to ligate the segment\n (-1 for ligating at the end)",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaIndex.place(x=20,y=360)

	#defining functions
	def back():
		window.destroy()
		main()

	def ligate_local():
		dna_seq = check_DNA_validity(dnaSeqInput1.get())
		dna_segment = check_DNA_validity(dnaSeqInput2.get())
		dna_index = dnaSeqIndex.get()
		if dna_seq == '' or dna_segment == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq or not dna_segment:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		if dna_index == '':
			user_response = messagebox.showwarning(title='No Index',message='Please Enter an Index!')
			return
		if dna_index.isdigit() == True or dna_index == '-1':
			if not(len(dna_seq) > int(dna_index) >= -1):
				user_response = messagebox.showwarning(title='Invalid Index',message='Invalid Index!')
				return
		else:
			user_response = messagebox.showwarning(title='Invalid Index',message='Invalid Index!')
			return

		feature_output = ligate(dna_segment , dna_seq,int(dna_index))
		user_response = messagebox.showinfo(title='Is Palindrome?',message=f'Your Segment after ligation > {feature_output}')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile1():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput1.insert(END, dna_seq)

	def openDNAfile2():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput2.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	ligateBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Ligate",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=ligate_local)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA1 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile1,bg="white")
	button_openFileDNA2 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile2,bg="white")

	#displaying buttons
	button_openFileDNA1.place(x=250,y=220)
	button_openFileDNA2.place(x=250,y=320)
	ligateBtn.place(x=360,y=540)
	back.place(x=360,y=600)

	#defining input fields
	dnaSeqInput1 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput1.place(x=20,y=220)
	dnaSeqInput2 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput2.place(x=20,y=320)
	dnaSeqIndex = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqIndex.place(x=20,y=420)

	window.mainloop()

def palindrome():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

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
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def palindrome():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output = ' ' if is_palindrome(dna_seq) else ' NOT '
		user_response = messagebox.showinfo(title='Is Palindrome?',message=f'Your strand is{feature_output}a palindrome!')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	palindromeBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Is Palindrome?",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=palindrome)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	palindromeBtn.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()

def gc_content():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

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
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def cgContent():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output = cg_content(dna_seq)
		user_response = messagebox.showinfo(title='GC Content',message=f'Your GC Content is: {feature_output}%')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	gcContentBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="GC Content",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=cgContent)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	gcContentBtn.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()


def complement():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

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
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def complement():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output = complement_DNA(dna_seq)
		user_response = messagebox.showinfo(title='Complementary Strad',message=f'Your complementary strand is: {feature_output}')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	complementbtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Complementary Strand",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=complement)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	complementbtn.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()

def count_nuc():

	#opening a window
	window = Tk()

	#file initiation
	#def openFile():
	#	window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))

	#naming the title of the program
	window.title("PySequence - Version 1.0 / Single Strand Analysis")

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
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def count():
		dna_seq = check_DNA_validity(dnaSeqInput.get())
		if dna_seq == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		feature_output_1 = number_of_each_nucleotide(dna_seq)
		feature_output_2 = percentage_of_each_nucleotide(dna_seq)
		user_response = messagebox.showinfo(title='Nucleotides Count & Percentages',message=f'[G,C,T,A] Count: {feature_output_1}\n[G,C,T,A] Percentages: {feature_output_2}')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		dna_file = open(file_path, 'r')
		dna_seq = check_DNA_validity(dna_file.readline())
		if not dna_seq:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return
		dnaSeqInput.insert(END, dna_seq)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	count = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=count)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	count.place(x=360,y=240)
	back.place(x=360,y=300)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()


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

	def count_nuc_local():
		window.destroy()
		count_nuc()

	def complement_local():
		window.destroy()
		complement()

	def gc_content_local():
		window.destroy()
		gc_content()

	def palindrome_local():
		window.destroy()
		palindrome()

	def ligate_local():
		window.destroy()
		ligate_sub()

	def search_segment_local():
		window.destroy()
		search_segment_sub()

	def count_segment_local():
		window.destroy()
		count_segment_sub()

	def reverse_complement_local():
		window.destroy()
		reverse_complement_sub()

	#defining buttons
	count = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=count_nuc_local)
	complementbtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Complementary Strand",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=complement_local)
	gcContent = Button(window, relief="solid",borderwidth=4, padx=40, text="G-C Content",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=gc_content_local)
	palindromeBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Palindrome?",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=palindrome_local)
	ligateBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Ligate a Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=ligate_local)
	segmentSearch = Button(window, relief="solid",borderwidth=4, padx=40, text="Search for Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=search_segment_local)
	segmentCount = Button(window, relief="solid",borderwidth=4, padx=40, text="Count Segment",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=count_segment_local)
	reverseComplement = Button(window, relief="solid",borderwidth=4, padx=40, text="Reverse Complementary",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=reverse_complement_local)
	reverseTranscriptase = Button(window, relief="solid", borderwidth=4, padx=40, text="Reverse Transcriptase",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan")
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=homepage)
	#openFileLabel = Button(window, relief="solid", borderwidth=4, padx=30, text="Open File",width=12,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=openFile)

	#defining input fields and file navigation
	# dnaInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=30)
	# dnaInput.place(x=20,y=220)

	#displaying buttons
	count.place(x=360,y=100)
	complementbtn.place(x=360,y=160)
	gcContent.place(x=360,y=220)
	palindromeBtn.place(x=360,y=280)
	ligateBtn.place(x=360,y=340)
	segmentSearch.place(x=360,y=400)
	segmentCount.place(x=360,y=460)
	reverseComplement.place(x=360,y=520)
	reverseTranscriptase.place(x=360,y=580)
	back.place(x=360,y=640)
	#openFileLabel.place(x=20,y=300)

	#running the program
	window.mainloop()
