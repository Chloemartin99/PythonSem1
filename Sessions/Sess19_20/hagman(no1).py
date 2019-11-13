from tkinter import *

def updateImage(image_counter):
    image_counter+=1
    lb = Label(master=window, text="si", font=font)
    lb.grid(row=20, column=20)

window = Tk()
window.title("Hangman by Chloe Martin")

font = ("Helvetica", 16)

lb = Label(master=window, text="A Hangman's Story", font=("Helvetica", 25), fg="blue")
lb.grid(row=1, column=5, padx=20, pady=20)

bt = Button(master=window, text="Exit", fg="red", font=("Helvetica", 13), command=sys.exit)
bt.grid(row=0, column=6)

lb = Label(master=window, text="Word: ", font=font)
lb.grid(row=4, column=3)

word = "rabbits"
positions = []

for i in range(len(word)):
    positions.append("_")

lb_pos = Label(master=window, text=positions, font=("Helvetica", 20))
lb_pos.grid(row=4, column=4)

lb = Label(master=window, text="Choose Letter:", font=font)
lb.grid(row=6, columnspan=3)

image_counter = 0
def checkLetter():
    choice = bta.cget('text')
    lb = Label(master=window, text=choice, font=font)
    lb.grid(row=50, columnspan=50)
    if choice in word:
        pass

    else:
        lb = Label(master=window, text=choice, font=font)
        lb.grid(row=30, column=30)
        updateImage(image_counter)

dict_buttons = {}
btb = Button(master=window, text="a", font=font, command=checkLetter)
btb.grid(row=7, column=0)
btb = Button(master=window, text="b", font=font, command=checkLetter)
btb.grid(row=7, column=1)
btb = Button(master=window, text="c", font=font, command=checkLetter)
btb.grid(row=7, column=2)
btb = Button(master=window, text="d", font=font, command=checkLetter)
btb.grid(row=8, column=0)
btb = Button(master=window, text="e", font=font, command=checkLetter)
btb.grid(row=8, column=1)
btb = Button(master=window, text="f", font=font, command=checkLetter)
btb.grid(row=8, column=2)
btb = Button(master=window, text="g", font=font, command=checkLetter)
btb.grid(row=9, column=0)
btb = Button(master=window, text="h", font=font, command=checkLetter)
btb.grid(row=9, column=1)
btb = Button(master=window, text="i", font=font, command=checkLetter)
btb.grid(row=9, column=2)
btb = Button(master=window, text="j", font=font, command=checkLetter)
btb.grid(row=10, column=0)
btb = Button(master=window, text="k", font=font, command=checkLetter)
btb.grid(row=10, column=1)
btb = Button(master=window, text="l", font=font, command=checkLetter)
btb.grid(row=10, column=2)
btb = Button(master=window, text="m", font=font, command=checkLetter)
btb.grid(row=11, column=0)
btb = Button(master=window, text="n", font=font, command=checkLetter)
btb.grid(row=11, column=1)
btb = Button(master=window, text="o", font=font, command=checkLetter)
btb.grid(row=11, column=2)
btb = Button(master=window, text="p", font=font, command=checkLetter)
btb.grid(row=12, column=0)
btb = Button(master=window, text="q", font=font, command=checkLetter)
btb.grid(row=12, column=1)
btb = Button(master=window, text="r", font=font, command=checkLetter)
btb.grid(row=12, column=2)
btb = Button(master=window, text="s", font=font, command=checkLetter)
btb.grid(row=13, column=0)
btb = Button(master=window, text="t", font=font, command=checkLetter)
btb.grid(row=13, column=1)
btb = Button(master=window, text="u", font=font, command=checkLetter)
btb.grid(row=13, column=2)
btb = Button(master=window, text="v", font=font, command=checkLetter)
btb.grid(row=14, column=0)
btb = Button(master=window, text="w", font=font, command=checkLetter)
btb.grid(row=14, column=1)
btb = Button(master=window, text="x", font=font, command=checkLetter)
btb.grid(row=14, column=2)
btb = Button(master=window, text="y", font=font, command=checkLetter)
btb.grid(row=15, column=0)
btb = Button(master=window, text="z", font=font, command=checkLetter)
btb.grid(row=15, column=1)

#normal_letters="abcdefghijklmnopqrstuvwxyz"
#x=0
#y=7
#buttons = []
#for i in range(len(normal_letters)):
 #   bt = Button(master=window, text=normal_letters[i], font=font, command=checkLetter)
  #  bt.grid(row=y, column=x)
   # buttons.append(bt)
    #x+=1
    #if x==3:
     #   x=0
      #  y += 1

window.mainloop()