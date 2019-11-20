import random
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

class Hangman(object):
    def __init__(self, window):
        self.window = window
        self.window.title("Hangman by Chloe Martin")
        self.font = ("Helvetica", 40)

        db = sqlite3.connect("hangman_records.db")
        cur = db.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS hangman(id INTEGER PRIMARY KEY, word VARCHAR, trials INTEGER, result varchar)")
        db.commit()
        db.close()

        self.lb = Label(master=self.window, text="A Hangman's Story", font=("Helvetica", 60), fg="blue")
        self.lb.grid(row=1, column=2, padx=10, pady=5)

        self.bt = Button(master=self.window, text="Exit", fg="red", font=self.font, command=sys.exit)
        self.bt.grid(row=0, column=6)

        self.lb = Label(master=self.window, text="Word: ", font=self.font)
        self.lb.grid(row=3, column=1, sticky="e")

        self.bt = Button(master=self.window, text="Save Game", fg="red", font=self.font, command=self.saveGame)
        self.bt.grid(row=1, column=6)

        ran = random.randint(0, 1000)
        file = open("1-1000.txt", "r")
        temp = file.read().splitlines()
        pick = temp[ran]

        self.letters = list(pick)
        self.word = ""
        for i in range(len(self.letters)):
            self.word+=self.letters[i]

        self.image_counter = 0
        self.done = []

        self.positions = []

        for i in range(len(self.word)):
            self.positions.append("_")

        self.lb_pos = Label(master=self.window, text=self.positions, font=self.font, fg="blue")
        self.lb_pos.grid(row=3, column=2)

        self.lb = Label(master=self.window, text="Choose Letter:", font=self.font)
        self.lb.grid(row=8, column=1, sticky="e")

        let = "abcdefghijklmnopqrstuvwxyz"
        self.letter_choice = []
        for i in let:
            self.letter_choice.append(i)

        self.var_choose = StringVar(window)
        self.var_choose.set(self.letter_choice[0])

        self.op = OptionMenu(self.window, self.var_choose, *self.letter_choice)
        self.op.grid(row=8, column=2)
        self.op.config(font=self.font)

        self.trials = 0

        self.bt = Button(master=self.window, text="GO!", font=self.font, command=self.checkLetter)
        self.bt.grid(row=9, column=2)

        self.canvas = Canvas(window, width=420, height=520)
        im = Image.open("S0.jpeg")
        size = 600, 520
        im.thumbnail(size)

        self.canvas.image = ImageTk.PhotoImage(im)
        self.canvas.create_image(220, 6, image=self.canvas.image, anchor="n")
        self.canvas.grid(row=9, column=6)

    def checkLetter(self):
        self.checkVictory()
        if self.var_choose.get() not in self.done:
            if self.var_choose.get() in self.letters:
                p = self.letters.index(self.var_choose.get())
                self.positions[p] = self.var_choose.get()

                temp = self.letters
                temp[p] = "-"
                if self.var_choose.get() in temp:
                    p2 = temp.index(self.var_choose.get())
                    self.positions[p2] = self.var_choose.get()

                self.lb_pos = Label(master=self.window, text=self.positions, font=self.font, fg="blue")
                self.lb_pos.grid(row=3, column=2)

            else:
                self.done.append(self.var_choose.get())
                txt = ""
                for i in range(len(self.done)):
                    txt += self.done[i] + '\u0336' + "  "

                    self.lb = Label(master=self.window, text=txt, font=self.font)
                    self.lb.grid(row=9, column=1)
                self.updateImage()
            self.trials += 1

    def checkVictory(self):
        correct_letters = ""
        for i in self.positions:
            correct_letters += i

        print(correct_letters)
        if correct_letters == self.word:
            self.lb = Label(master=self.window, text="***VICTORY!***", font=("Helvetica", 50), fg="green")
            self.lb.grid(row=7, column=1)
            return True
        return False

    def updateImage(self):
        self.image_counter += 1

        if self.image_counter <= 13:
            im2 = Image.open("S" + str(self.image_counter) + ".jpeg")
            size = 600, 520
            im2.thumbnail(size)
            self.canvas.image = ImageTk.PhotoImage(im2)
            self.canvas.create_image(220, 6, image=self.canvas.image, anchor="n")

        elif self.checkVictory() is False:
            self.lb = Label(master=self.window, text="The word was " + self.word, font=self.font, fg="red")
            self.lb.grid(row=12, column=1)

    def saveGame(self):
        result = ""
        if self.checkVictory() is True:
            result = "Won"
        else:
            result = "Lost"

        db = sqlite3.connect("hangman_records.db")
        cur = db.cursor()
        cur.execute("INSERT INTO hangman VALUES(NULL, ?, ?, ?)", (self.word, self.trials, result))
        db.commit()
        db.close()

window = Tk()
h = Hangman(window)
print(h.word)
window.mainloop()