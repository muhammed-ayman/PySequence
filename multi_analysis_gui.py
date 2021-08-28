#importing tkinter modules
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog
from main_imports import *
import analyze_gui

def checkSequenceTypeSimilarity(seq_one, seq_two):
    seq_one_type = 'DNA'
    seq_two_type = 'DNA'
    if check_RNA_validity(seq_one) and not (check_DNA_validity(seq_one)):
        seq_one_type = 'RNA'
    if check_RNA_validity(seq_two) and not (check_DNA_validity(seq_two)):
        seq_two_type = 'RNA'
    if seq_one_type != seq_two_type:
        return (False , seq_one_type)

    return (True , seq_one_type)

def most_matching_nuc_sub():

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
	dnaInputLabel1 = Label(window, padx=20, pady=10, text="Enter the First Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel1.place(x=20,y=160)
	dnaInputLabel2 = Label(window, padx=20, pady=10, text="Enter the Second Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel2.place(x=20,y=260)

	#defining functions
	def back():
		window.destroy()
		main()

	def most_matching_nuc_local():
		genomic_seq_one = dnaSeqInput1.get()
		genomic_seq_two = dnaSeqInput2.get()
		if genomic_seq_one == '' or genomic_seq_two == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not(check_DNA_validity(genomic_seq_one) or check_RNA_validity(genomic_seq_one)) or not(check_DNA_validity(genomic_seq_two) or check_RNA_validity(genomic_seq_two)):
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return

		similarity_type_check = checkSequenceTypeSimilarity(genomic_seq_one, genomic_seq_two)
		if not(similarity_type_check[0]):
			user_response = messagebox.showwarning(title='Invalid Type',message='The two Sequences should be of the same type!')
			return

		feature_output = most_matching_nucleotides(genomic_seq_one, genomic_seq_two, similarity_type_check[1])
		if len(feature_output) > 1:
			user_response = messagebox.showinfo(title='Most Matching Nucleotides',message=f'The most matching nucleotides are {feature_output}')
		elif len(feature_output) == 1:
			user_response = messagebox.showinfo(title='Most Matching Nucleotides',message=f'The most matching nucleotide is {feature_output[0]}')
		else:
			user_response = messagebox.showinfo(title='No Matching Nucleotides',message=f'There are no matching nucleotides!')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile1():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		genomic_file = open(file_path, 'r')
		seq_one = genomic_file.readline()
		dnaSeqInput1.insert(END, seq_one)

	def openDNAfile2():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return
		genomic_file = open(file_path, 'r')
		seq_one = genomic_file.readline()
		dnaSeqInput2.insert(END, seq_one)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	matchSimilarityBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Most Matching Nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=most_matching_nuc_local)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA1 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile1,bg="white")
	button_openFileDNA2 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile2,bg="white")

	#displaying buttons
	button_openFileDNA1.place(x=250,y=220)
	button_openFileDNA2.place(x=250,y=320)
	matchSimilarityBtn.place(x=360,y=540)
	back.place(x=360,y=600)

	#defining input fields
	dnaSeqInput1 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput1.place(x=20,y=220)
	dnaSeqInput2 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput2.place(x=20,y=320)

	window.mainloop()

def most_matching_seqs_sub():

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
	dnaInputLabel = Label(window, padx=20, pady=10, text="Enter the file containing your Sequences",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel.place(x=20,y=160)

	#defining functions
	def back():
		window.destroy()
		main()

	def most_matching_seqs_local():
		dna_file = two_closest_sequences(dnaSeqInput.get())
		if not dna_file:
			user_response = messagebox.showwarning(title='Invalid Path',message='Invalid Path!')
			return

		if len(dna_file[0]) > 0:
			user_response = messagebox.showinfo(title='Most Matching RNA Sequences',message=f'The most matching RNA sequences are {dna_file[0][0]}')
		if len(dna_file[1]) > 0:
			user_response = messagebox.showinfo(title='Most Matching DNA Sequences',message=f'The most matching DNA sequences are {dna_file[1][0]}')
			return
		user_response = messagebox.showwarning(title='No Matching Sequences!',message='No Matching Sequences!\nCheck your File')

	#file initiation
	def openFile():
		window.filename = filedialog.askopenfilename(title="Choose file",filetypes=(("txt files","*.txt"),("All Types (*txt)","*.txt")))
		return window.filename

	def openDNAfile():
		file_path = openFile()
		if not os.path.isfile(file_path):
			return

		dnaSeqInput.insert(END, file_path)

	#defining image to be used as an icon for file navigation
	fileImage = PhotoImage(file="Images/Folder_Icon_32.png")

	#defining buttons
	mostMatchingBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Most Matching Sequences",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=most_matching_seqs_local)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA = Button(window,borderwidth=0,image=fileImage,command=openDNAfile,bg="white")

	#displaying buttons
	button_openFileDNA.place(x=250,y=220)
	mostMatchingBtn.place(x=360,y=540)
	back.place(x=360,y=600)

	#defining input fields
	dnaSeqInput = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput.place(x=20,y=220)

	window.mainloop()

def matching_per_sub():

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
	dnaInputLabel1 = Label(window, padx=20, pady=10, text="Enter the First DNA Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel1.place(x=20,y=160)
	dnaInputLabel2 = Label(window, padx=20, pady=10, text="Enter the Second DNA Sequence",font="Helvetica 16 bold italic",fg="dark blue",bg="white")
	dnaInputLabel2.place(x=20,y=260)

	#defining functions
	def back():
		window.destroy()
		main()

	def match_similarity_local():
		dna_seq_one = check_DNA_validity(dnaSeqInput1.get())
		dna_seq_two = check_DNA_validity(dnaSeqInput2.get())
		if dna_seq_one == '' or dna_seq_two == '':
			user_response = messagebox.showwarning(title='No Sequence',message='Please Enter a Sequence!')
			return
		if not dna_seq_one or not dna_seq_two:
			user_response = messagebox.showwarning(title='Invalid Sequence',message='Invalid Sequence!')
			return

		feature_output = round(sequences_matching_percentage(dna_seq_one, dna_seq_two),2)
		user_response = messagebox.showinfo(title='Matching Percentage',message=f'The sequences matching percentage is {feature_output}%')

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
	matchSimilarityBtn = Button(window, relief="solid",borderwidth=4, padx=40, text="Matching Percentage",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=match_similarity_local)
	back = Button(window, relief="solid", borderwidth=4, padx=40, text="Back",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=back)
	button_openFileDNA1 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile1,bg="white")
	button_openFileDNA2 = Button(window,borderwidth=0,image=fileImage,command=openDNAfile2,bg="white")

	#displaying buttons
	button_openFileDNA1.place(x=250,y=220)
	button_openFileDNA2.place(x=250,y=320)
	matchSimilarityBtn.place(x=360,y=540)
	back.place(x=360,y=600)

	#defining input fields
	dnaSeqInput1 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput1.place(x=20,y=220)
	dnaSeqInput2 = Entry(window,font="Helvetica 11 bold italic",bg="White",fg="dark blue",bd=3,relief="solid",width=25)
	dnaSeqInput2.place(x=20,y=320)

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

	def matching_per_local():
		window.destroy()
		matching_per_sub()

	def most_matching_seqs_local():
		window.destroy()
		most_matching_seqs_sub()

	def most_matching_nuc_local():
		window.destroy()
		most_matching_nuc_sub()

	#defining buttons
	matching_percentage = Button(window, relief="solid",borderwidth=4, padx=40, text="Matching Percentage",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=matching_per_local)
	matching_sequences = Button(window, relief="solid",borderwidth=4, padx=40, text="Most matching sequences",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=most_matching_seqs_local)
	matching_nucleotides = Button(window, relief="solid",borderwidth=4, padx=40, text="Most matching nucleotides",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=most_matching_nuc_local)
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
