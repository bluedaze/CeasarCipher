from tkinter import *
from tkinter import ttk

def get_message(*args):
    value = message.get()
    print(value)

def get_scale(*args):
    value = scale.get()
    slider.set(value)
    print(value)

root = Tk()
root.title("Ceasar Cipher example program")


########## Variable inits ##########
message = StringVar()
mode = StringVar()
key = StringVar()
slider = StringVar()
scale = IntVar()

########## Style settings ##########
s = ttk.Style()
s.theme_use("classic")
s.configure('.', background="black", foreground="white")
message_style = ttk.Style()
message_style.configure("My.TEntry", fieldbackground="black", background="black", foreground="white")

########## Frame inits ##########
main_frame = ttk.LabelFrame(root, text="[Box box]")
main_frame["padding"] = (5, 5)
bubble_frame = ttk.Frame(main_frame)
box_frame = ttk.Frame(main_frame)
key_frame = ttk.LabelFrame(main_frame, text="Choose a key: ")
log_frame = ttk.LabelFrame(main_frame, text="Transcription: ")



########## Widget inits ##########
message_box = ttk.Entry(box_frame, width=40, textvariable=message)
message_box.configure(style="My.TEntry")

encrypt = ttk.Radiobutton(bubble_frame, text='Encrypt', variable=mode, value='encrypt')
decrypt = ttk.Radiobutton(bubble_frame, text='Decrypt', variable=mode, value='decrypt')

key_slider = ttk.Scale(key_frame, orient=HORIZONTAL, variable=scale, length=195, from_=0.0, to=40.0, command=get_scale)
key_label = Label(key_frame, textvariable=slider, width=3)

log = Text(log_frame, height=1, width=45, background="black", foreground="white", state='disabled')

########## Widget methods ##########
message_box.insert(0, "Enter a message")

########## Grid Settings ##########
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=0)
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))


bubble_frame.grid(column=0, row=0)
encrypt.grid(column=0, row=0, ipadx=2, sticky=W)
decrypt.grid(column=0, row=1, ipadx=2, sticky=W)

key_frame.grid(column=1, row=0, sticky=S)
key_slider.grid(column=2, pady=5, padx=5,  row=3)
key_label.grid(column=1, padx=5,  row=3)

box_frame.grid(column=0, columnspan=3, row=2, sticky=S)
message_box.grid(column=0, ipadx=5, row=2, sticky=W)

log_frame.grid(column=0, columnspan=3, row=3, sticky=S)
log.grid(column=0, pady=5, padx=5,)


for child in main_frame.winfo_children():
    child.grid_rowconfigure(0, weight=0)
    child.grid_columnconfigure(0, weight=0)
    child.grid_configure(padx=5, pady=5)


message_box.focus()
root.bind('<Return>', get_message)
root.mainloop()
