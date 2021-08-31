from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import ImageTk, Image
from constants import *

# This is an abstract class that all window classes inherit
class View():
    def __init__(self):
        self.window = Tk()
        self.window_specifications = {
            'geometry': GEOMETRY
        }

    def render_font(self,font_name,font_size):
        font = tkFont.Font(family=font_name, size=font_size)
        return font

    def exit(self):
        exit_user_response = messagebox.askyesno("Confirmation","Are you sure you want to exit?")
        if exit_user_response == 1:
            exit()
        else:
            return


class Analyze(View):
    def render(self):
        self.window.geometry(self.window_specifications['geometry'])
        self.window.title(MAIN_TITLE)
        self.window.resizable(0,0)
        self.window.configure(background=BACKGROUND_COLOR)
        self.program_title = Label(self.window,
                        text=PROGRAM_TITLE,
                        padx=20, pady=20,
                        font=self.render_font('Lucida Grande', 20),
                        fg="dark red",
                        bg="white")
        self.button_single_strand = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Single Strand Analysis",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.single_strand_window)
        self.button_multi_strand = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Multi Strand Analysis",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.multi_strand_window)
        self.button_back = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Back",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.main_window)

        self.display_objects()
        self.window.mainloop()

    def display_objects(self):
        self.program_title.grid(row=0, column=0)
        self.button_single_strand.place(x=360,y=100)
        self.button_multi_strand.place(x=360,y=190)
        self.button_back.place(x=360,y=280)

    def single_strand_window(self):
        pass

    def multi_strand_window(self):
        pass

    def main_window(self):
        self.window.destroy()
        main_instance = Main()
        main_instance.render()

class CentralDogma(View):
    def __init__(self):
        super().__init__()
        self.window_specifications = {
            'geometry': '750x500'
        }

    def render(self):
        self.window.geometry(self.window_specifications['geometry'])
        self.window.title(MAIN_TITLE)
        self.window.resizable(0,0)
        self.window.configure(background=BACKGROUND_COLOR)
        self.program_title = Label(self.window,
                        text=PROGRAM_TITLE,
                        padx=20, pady=20,
                        font=self.render_font('Lucida Grande', 20),
                        fg="dark red",
                        bg="white")
        self.button_transcription = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Transcribe DNA",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.transcribe_dna)
        self.button_translation = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Translate DNA",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.translate_dna)
        self.button_automate_central_dogma = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Automate Central Dogma",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.automate_central_dogma)
        self.button_back = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Back",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.main_window)
        self.open_folder_img = PhotoImage(file=f"{ASSETS_FOLDER_PATH}{OPEN_FOLDER_IMG}")
        self.button_open_dna_file = Button(self.window,
                        borderwidth=0,
                        image=self.open_folder_img,
                        command=self.open_dna_file,
                        bg="white")
        self.button_open_rna_file = Button(self.window,
                        borderwidth=0,
                        image=self.open_folder_img,
                        command=self.open_rna_file,
                        bg="white")
        self.input_dna_seq = Entry(self.window,
                        font="Helvetica 11 bold italic",
                        bg="White",
                        fg="dark blue",
                        bd=3,
                        relief="solid",
                        width=25)
        self.input_rna_seq = Entry(self.window,
                        font="Helvetica 11 bold italic",
                        bg="White",
                        fg="dark blue",
                        bd=3,
                        relief="solid",
                        width=25)

        self.display_objects()
        self.window.mainloop()

    def display_objects(self):
        self.program_title.grid(row=0, column=0)
        self.button_transcription.place(x=360,y=100)
        self.button_translation.place(x=360,y=190)
        self.button_open_dna_file.place(x=250,y=220)
        self.button_open_rna_file.place(x=250,y=390)
        self.input_dna_seq.place(x=20,y=220)
        self.input_rna_seq.place(x=20,y=390)
        self.button_back.place(x=360,y=370)

    def transcribe_dna(self):
        pass

    def translate_dna(self):
        pass

    def automate_central_dogma(self):
        pass

    def open_dna_file(self):
        pass

    def open_rna_file(self):
        pass

    def main_window(self):
        self.window.destroy()
        main_instance = Main()
        main_instance.render()

class Manual(View):
    def __init__(self):
        super().__init__()
        self.window_specifications = {
            'geometry': '900x630'
        }
        self.manual_imgs_names = [
            'pairings.png',
            'centralDogma.png',
            'polypeptide.png',
            'translation.png'
        ]
        self.manual_imgs = [

        ]
        self.current_img = 0

    def render(self):
        self.window.geometry(self.window_specifications['geometry'])
        self.window.title(MAIN_TITLE)
        self.window.resizable(0,0)
        self.window.configure(background=BACKGROUND_COLOR)
        self.program_title = Label(self.window,
                        text=PROGRAM_TITLE,
                        padx=20, pady=20,
                        font=self.render_font('Lucida Grande', 20),
                        fg="dark red",
                        bg="white")
        self.button_right = Button(self.window,
                        pady=5,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        relief="solid",
                        width=10, height=2,
                        command=self.swipe_right,
                        text="Swipe Right")
        self.button_left = Button(self.window,
                        pady=5,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        relief="solid",
                        width=10, height=2,
                        command=self.swipe_left,
                        text="Swipe Left")
        self.button_back = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Back",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.main_window)

        self.render_imgs()
        if len(self.manual_imgs) > 0:
            self.MainLabel = Label(image=self.manual_imgs[0])

        self.display_objects()
        self.window.mainloop()

    def display_objects(self):
        self.program_title.grid(row=0, column=0)
        self.button_left.grid(row=3,column=2)
        self.button_right.grid(row=3,column=4)
        self.button_back.grid(row=3,column=3)
        self.display_main_label()
        self.disable_swipe_buttons()

    def display_main_label(self):
        self.MainLabel.grid(row=2,column=2,columnspan=3)

    def disable_swipe_buttons(self):
        if self.current_img == 0:
            self.button_left['state'] = DISABLED
        else:
            self.button_left['state'] = NORMAL

        if self.current_img == len(self.manual_imgs)-1:
            self.button_right['state'] = DISABLED
        else:
            self.button_right['state'] = NORMAL

    def render_imgs(self):
        for img_name in self.manual_imgs_names:
            img = ImageTk.PhotoImage(Image.open(f"{ASSETS_FOLDER_PATH}/{img_name}"))
            self.manual_imgs.append(img)

    def swipe_right(self):
        self.current_img += 1
        self.disable_swipe_buttons()
        self.MainLabel.grid_forget()
        self.MainLabel = Label(image=self.manual_imgs[self.current_img])
        self.display_main_label()

    def swipe_left(self):
        self.current_img -= 1
        self.disable_swipe_buttons()
        self.MainLabel.grid_forget()
        self.MainLabel = Label(image=self.manual_imgs[self.current_img])
        self.display_main_label()

    def main_window(self):
        self.window.destroy()
        main_instance = Main()
        main_instance.render()


class Main(View):
    def render(self):
        self.window.geometry(self.window_specifications['geometry'])
        self.window.title(MAIN_TITLE)
        self.window.resizable(0,0)
        self.window.configure(background=BACKGROUND_COLOR)
        self.program_title = Label(self.window,
                        text=PROGRAM_TITLE,
                        padx=20, pady=20,
                        font=self.render_font('Lucida Grande', 20),
                        fg="dark red",
                        bg="white")
        self.button_analyze = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Analyze",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.analyze_window)
        self.button_central_dogma = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Transcribe / Translate",
                        width=15,font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.cdogmae_window)
        self.button_manual = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Manual",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.manual_window)
        self.button_exit = Button(self.window,
                        relief="solid",
                        borderwidth=4,
                        padx=40, pady=20,
                        text="Exit",
                        width=15,
                        font="Helvetica 16 bold italic",
                        fg="dark blue",
                        bg="dark cyan",
                        command=self.exit)

        self.display_objects()
        self.window.mainloop()

    def display_objects(self):
        self.program_title.grid(row=0, column=0)
        self.button_analyze.place(x=360,y=100)
        self.button_central_dogma.place(x=360,y=190)
        self.button_manual.place(x=360,y=280)
        self.button_exit.place(x=360,y=370)

    def analyze_window(self):
        self.window.destroy()
        analyze_instance = Analyze()
        analyze_instance.render()

    def manual_window(self):
        self.window.destroy()
        manual_instance = Manual()
        manual_instance.render()

    def cdogmae_window(self):
        self.window.destroy()
        central_dogma_instance = CentralDogma()
        central_dogma_instance.render()

if __name__ == '__main__':
    app = Main()
    app.render()
