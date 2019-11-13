from tkinter import *

window = Tk()
window.title("Hangman by Chloe Martin")

font = ("Helvetica", 16)

lb = Label(master=window, text="A Hangman's Story", font=("Helvetica", 25), fg="blue")
lb.grid(row=1, column=3, padx=20, pady=20)

bt = Button(master=window, text="Exit", fg="red", font=("Helvetica", 13), command=sys.exit)
bt.grid(row=0, column=6)

lb = Label(master=window, text="Word: ", font=font)
lb.grid(row=4, column=0)

word = "rabbit"
positions = []

for i in range(len(word)):
    positions.append("_")

lb_pos = Label(master=window, text=positions, font=("Helvetica", 20))
lb_pos.grid(row=4, column=1)

lb = Label(master=window, text="Enter Letter:", font=font)
lb.grid(row=6, column=0)

normal_letters="abcdefghijklmnopqrstuvwxyz"
crossed_letters="̶a̶b̶c̶d̶e̶f̶g̶h̶i̶j̶k̶l̶m̶n̶o̶p̶q̶r̶s̶t̶u̶v̶w̶x̶y̶z"
letter_dic = {}
for i in range(len(normal_letters)):
    letter_dic[i]=crossed_letters[i]


image_counter= 0
chosen_letters = ""

def updateImage(image_counter):
    image_counter+=1

def checkLetter(chosen_letters):
    entrymade = et.get()[]
    if entrymade in word:
        positions[word.index(entrymade)]=str(et)
        lb = Label(master=window, textvariable="siii")
        lb.grid(row=12, column=0)

    else:
        chosen_letters = letter_dic[input_letter] + " "
        lb = Label(master=window, text=chosen_letters, font=font)
        lb.grid(row=10, column=1)
    window.update_idletasks()

input_letter = StringVar(window)
et = Entry(master=window, textvariable=input_letter, font=("Helvetica", 20), fg="blue")
et.grid(row=6, column=1)

bt = Button(master=window, text="GO!", fg="blue", command=checkLetter(chosen_letters))
bt.grid(row=8, column=1)

window.mainloop()