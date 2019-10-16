from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Ceasar Cipher example program")


########## Style settings ##########
s = ttk.Style()
s.theme_use("classic")
s.configure('.', background="black", foreground="white")




########## Frame inits ##########
main_frame = ttk.LabelFrame(root, text="[Box box]")
main_frame["padding"] = (5, 5)
main_frame["borderwidth"] = 5
main_frame["relief"] = "sunken"
bubble_frame = ttk.Frame(main_frame)
box_frame = ttk.Frame(main_frame)
key_frame = ttk.LabelFrame(main_frame, text="[Your chosen key: RandomVar]")

########## Variable inits ##########
message = StringVar()
mode = StringVar()
key = StringVar()

########## Widget inits ##########
message_box = ttk.Entry(box_frame, width=30, textvariable=message)
message_box.focus()
encrypt = ttk.Radiobutton(bubble_frame, text='Encrypt', variable=mode, value='encrypt')
decrypt = ttk.Radiobutton(bubble_frame, text='Decrypt', variable=mode, value='decrypt')
key_slider = ttk.Scale(key_frame, orient=HORIZONTAL, length=330, from_=0.0, to=100.0)

########## Grid Settings ##########
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=0)
bubble_frame.grid(column=0, row=0)
box_frame.grid(column=1, row=0, ipady=6, sticky=S)
message_box.grid(column=0, row=2, ipadx=5, sticky=S)
encrypt.grid(column=0, row=0, sticky=W)
decrypt.grid(column=0, row=1, sticky=W)
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
key_frame.grid(column=0, columnspan=3,row=4, sticky=S)
key_slider.grid(column=0, columnspan=3,  pady=5, padx=5,  row=3)


for child in main_frame.winfo_children():
    child.grid_rowconfigure(0, weight=0)
    child.grid_columnconfigure(0, weight=0)
    child.grid_configure(padx=5, pady=5)

root.mainloop()
