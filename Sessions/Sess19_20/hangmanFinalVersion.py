import random
from tkinter import *
from PIL import ImageTk, Image

def checkLetter():
    global done
    global letter_choice
    if var_choose.get() not in done:
        done.append(var_choose.get())

    txt = ""
    for i in range(len(done)):
        txt+=done[i]+'\u0336'+"  "

        lb = Label(master=window, text=txt, font=font)
        lb.grid(row=9, column=1)

    if var_choose.get() in word:
        p = word.index(var_choose.get())
        positions[p] = var_choose.get()

        temp = word
        temp[p]="-"
        if var_choose.get() in temp:
            p2 = temp.index(var_choose.get())
            positions[p2] = var_choose.get()

        lb_pos = Label(master=window, text=positions, font=font, fg="blue")
        lb_pos.grid(row=3, column=2)
    else:
        updateImage()
    checkHealth()
def updateImage():
    global image_counter
    image_counter+=1

    if image_counter<=13:
        im2 = Image.open("S" + str(image_counter) + ".jpeg")
        size = 600, 520
        im2.thumbnail(size)
        canvas.image= ImageTk.PhotoImage(im2)
        canvas.create_image(220, 6, image=canvas.image, anchor="n")
    else:
        lb = Label(master=window, text="The word was " + word, font=font, fg="red")
        lb.grid(row=12, column=1)

def checkHealth(): #doesn't work
    pass
    #if image_counter==13:
     #   lb = Label(master=window, text="The word was "+word, font=font, fg="red")
      #  lb.grid(row=12, column=1)
       # return False
    #else:
     #   for i in positions:
      #      if i == "_":
       #         return False
    #lb = Label(master=window, text="VICTORY!", font=font, fg="green")
    #lb.grid(row=12, column=1)

window = Tk()
window.title("Hangman by Chloe Martin")

font = ("Helvetica", 40)

lb = Label(master=window, text="A Hangman's Story", font=("Helvetica", 60), fg="blue")
lb.grid(row=1, column=2, padx=10, pady=5)

bt = Button(master=window, text="Exit", fg="red", font=font, command=sys.exit)
bt.grid(row=0, column=6)

lb = Label(master=window, text="Word: ", font=font)
lb.grid(row=3, column=1, sticky="e")

random = random.randint(0, 1000)
file = open("1-1000.txt", "r")
temp = file.read().splitlines()
pick = temp[random]

word = list(pick)
image_counter = 0
done=[]

positions = []

for i in range(len(word)):
    positions.append("_")

lb_pos = Label(master=window, text=positions, font=font, fg="blue")
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
op.config(font=font)

bt = Button(master=window, text="GO!", font=font, command=checkLetter)
bt.grid(row=9, column=2)

canvas = Canvas(window, width=420, height=520)
im = Image.open("S0.jpeg")
size = 600,520
im.thumbnail(size)

canvas.image = ImageTk.PhotoImage(im)
canvas.create_image(220, 6, image=canvas.image, anchor="n")
canvas.grid(row=9, column=6)

window.mainloop()
window.close()