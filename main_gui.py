#importing tkinter modules
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import cdogma_gui

def main():

    #opening a window
    window = Tk()

    #naming the title of the program
    window.title("PySequence - Version 1.0")

    # Setting the geometry i.e Dimensions
    window.geometry("750x500")

    #disabling maximize and minimize buttons
    window.resizable(0,0)

    #changing background color
    window.configure(background="white")

    #font styling
    nameFontStyle = tkFont.Font(family="Lucida Grande", size=20)

    #defining labels
    name = Label(window,text="PySequence 1.0",padx=20,pady=20,font=nameFontStyle,fg="dark red",bg="white")

    #defining function to swipe pages
    def manualPage():
        window.destroy()
        import manual_gui

    def analyzepage():
    	window.destroy()
    	import analyze_gui

    def cdogmaepage():
    	window.destroy()
    	cdogma_gui.main()

    def exitAssurance():
    	userResponse = messagebox.askyesno("Confirmation","Are you sure you want to exit?")
    	if userResponse == 1:
            exit()
    	else:
    		return

    #defining buttons
    button_analyze = Button(window, relief="solid",borderwidth=4, padx=40, pady=20, text="Analyze",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=analyzepage)
    button_central_dogma = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Transcribe / Translate",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=cdogmaepage)
    button_manual = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Manual",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=manualPage)
    button_exit = Button(window, relief="solid", borderwidth=4, padx=40, pady=20, text="Exit",width=15,font="Helvetica 16 bold italic",fg="dark blue",bg="dark cyan",command=exitAssurance)

    #displaying labels
    name.grid(row=0, column=0)

    #displaying buttons
    button_analyze.place(x=360,y=100)
    button_central_dogma.place(x=360,y=190)
    button_manual.place(x=360,y=280)
    button_exit.place(x=360,y=370)

    #running the program until the user clicks "X"
    window.mainloop()

if __name__ == '__main__':
    main()
