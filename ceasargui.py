import tkinter as tk

WIDTH = 600
HEIGHT = 500

root = tk.Tk()

CANVAS = tk.Canvas(root, height=HEIGHT, width=WIDTH)

frame = tk.Frame(root, bg="black")
frame.place(relwidth = 1, relheight=1)

CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()


C1 = tk.Checkbutton(root, selectcolor="black", bg="black", fg="white",
text = "encrypt", variable = CheckVar1, onvalue = 1, offvalue = 0)
C1.place(x = 0.25, y=.25)


C2 = tk.Checkbutton(root, selectcolor="black", bg="black", fg="white",
text = "decrypt", variable = CheckVar2, onvalue = 1, offvalue = 0)
C2.place(x = 0.25, y=25)


message = tk.Label(root, bg="black", fg="white", font=("Helvetica", 10), text="Enter your message")
message.place(x = 100)

message_box = tk.Entry(root, bg="black", fg="white",)
message_box.place(x = 100, y = 25)


key_message = tk.Label(root, bg="black", fg="white", font=("Helvetica", 12), text="key value: ")
key_message.place(x = 1, y = 60)

key_value = tk.Entry(root, bg="black", fg="white",)
key_value.place(x = 100, y = 60, width = 28)





root.mainloop()
