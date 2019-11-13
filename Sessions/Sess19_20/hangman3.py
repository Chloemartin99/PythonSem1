from tkinter import *
from PIL import ImageTk, Image

def checkLetter():
    if var_choose.get() in word:
        positions[word.index(var_choose.get())] = var_choose.get()
        lb_pos = Label(master=window, text=positions, font=("Helvetica", 25), fg="blue")
        lb_pos.grid(row=4, column=4)
    else:
        updateImage()

def updateImage():
    global image_counter
    image_counter+=1

    im2 = Image.open("S" + str(image_counter) + ".jpeg")
    size = 360, 420
    im2.thumbnail(size)
    canvas.image= ImageTk.PhotoImage(im2)
    canvas.create_image(0, 0, image=canvas.image, anchor="n")

window = Tk()
window.title("Hangman by Chloe Martin")

font = ("Helvetica", 25)

lb = Label(master=window, text="A Hangman's Story", font=("Helvetica", 30), fg="blue")
lb.grid(row=1, column=2, padx=20, pady=20)

bt = Button(master=window, text="Exit", fg="red", font=("Helvetica", 25), command=sys.exit)
bt.grid(row=0, column=6)

lb = Label(master=window, text="Word: ", font=font)
lb.grid(row=3, column=1, sticky="e")

word = "rabbits"
image_counter = 0

positions = []

for i in range(len(word)):
    positions.append("_")

lb_pos = Label(master=window, text=positions, font=("Helvetica", 30), fg="blue")
lb_pos.grid(row=3, column=2)

lb = Label(master=window, text="Choose Letter:", font=font)
lb.grid(row=8, column=1, sticky="e")

let="abcdefghijklmnopqrstuvwxyz"
letter_choice = []
for i in let:
    letter_choice.append(i)

var_choose = StringVar(window)
var_choose.set(letter_choice[0])

op = OptionMenu(window, var_choose, *letter_choice)
op.grid(row= 8, column=2)
op.config(font=("Helvetica", 25))

bt = Button(master=window, text="GO!", font=font, command=checkLetter)
bt.grid(row=9, column=2)

canvas = Canvas(window, width=220, height=270, bg="red")
im = Image.open("S9.jpeg")
size = 300,270
im.thumbnail(size)

canvas.image = ImageTk.PhotoImage(im)
canvas.create_image(110, 3, image=canvas.image, anchor="n")
canvas.grid(row=9, column=4)


window.mainloop()