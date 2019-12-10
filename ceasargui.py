## I am using tkinter because it does not require user to download additional dependencies such as
## flask, django, kwin, kivy, pyQT etc. It is more or less native to Python. Also, tkinter is
## one of the few GUI frameworks available that is truly crossplatform. Many frames either work with
## windows natively, or Linux natives. Rarely both. :(

from tkinter import *
import tkinter as tk
from tkinter import ttk
import ceasarcipher as cc


class Encoding(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.mode = StringVar()
        self.mode.set(1)

        self.encrypt = ttk.Radiobutton(self, text='Encrypt', variable=self.mode, value='1', command=self.get_selected)
        self.decrypt = ttk.Radiobutton(self, text='Decrypt', variable=self.mode, value='2', command=self.get_selected)

        self.encrypt.grid(column=0, row=0, ipadx=2, sticky=W)
        self.decrypt.grid(column=0, row=1, ipadx=2, sticky=W)

    def get_selected(self, *args):
        mode = self.mode.get()
        if mode == "1":
            return "encrypt"
        elif mode == "2":
            return "decrypt"


class Key_code(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        ttk.LabelFrame.__init__(self, parent, *args, **kwargs)

        self.configure(text="Choose a key: ")

        self.scale = IntVar()
        self.slider = StringVar()

        self.key_slider = ttk.Scale(self, orient=HORIZONTAL, variable=self.scale, length=195, from_=0.0, to=40.0, command=self.get_scale)
        self.key_slider.grid(column=2, pady=5, padx=5,  row=0)

        self.key_label = tk.Label(self, textvariable=self.slider, width=2)
        self.key_label.grid(column=1, padx=5,  row=0)

    def get_scale(self, *args):
        key = self.scale.get()
        self.slider.set(key)
        return key


class Message(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        message_style = ttk.Style()
        message_style.configure("My.TEntry", fieldbackground="#020204", background="#020204", foreground="#00ff41")


        self.message = StringVar()



        self.message_box = ttk.Entry(self, width=45, textvariable=self.message)
        self.message_box.grid(column=0, ipadx=5, row=2, sticky=W)
        self.message_box.configure(style="My.TEntry")


    def get_message(self, *args):
        message = self.message.get()
        return message

class Transcription(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.output = tk.Text(self, height=2, width=50, background="#020204", foreground="white")
        self.output.grid(column=0, ipadx=10, row=2, sticky=W)

    def output(self, abc, *args):
        # uhhh, I dunno. This needs to exist otherwise the text widget doesn't work? But it literally has no reason to exist otherwise.
        pass


class MainApplication(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        ttk.LabelFrame.__init__(self, parent, *args, **kwargs)

        self.s = ttk.Style()
        self.s.theme_use("classic")
        self.s.configure('.', background="#020204", foreground="#00ff41")

        self.configure(text="Main Window")
        self['borderwidth'] = 3
        self['relief'] = 'raised'

        self.encoding = Encoding(self)
        self.encoding.grid(row=0, column=0)

        self.message = Message(self)
        self.message.grid(column=0, columnspan=2, row=1, sticky=S)

        self.key_code = Key_code(self)
        self.key_code.grid(row=0, column=1)

        self.transcription = Transcription(self)
        self.transcription.grid(column=0, columnspan=2, row=3)

        root.bind('<Return>', self.retrieve_values)

    def retrieve_values(self, *args):
        message = self.message.get_message()
        mode = self.encoding.get_selected()
        key = self.key_code.get_scale()
        cc_transcription = str(cc.ceasar_cipher(mode, message, key))
        self.transcription.output.delete('1.0', END)
        self.transcription.output.insert('1.0', cc_transcription)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
