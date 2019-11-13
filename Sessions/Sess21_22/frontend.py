from tkinter import *
import backend

class Front(object):
    def __init__(self, window):
        self.window = window #store the window in the object in order to be able to work with this window in other methods
        self.window.title("This is a fancy database project.")
        self.myfont = ("Times New Roman", 18) #as we are going to use the same font, we can create a font object.
        self.yourfont = ("Curier", 14)

        #need to create a backend instance here
        self.bk = backend.Back()

        #now lets create the widgets
        #labels: a label is not selectable

        self.lb1 = Label(master=self.window, text="Title", font=self.myfont)
        self.lb1.grid(row=0, column=0, sticky="w", pady=5)

        self.lb1 = Label(master=self.window, text="  Year", font=self.myfont)
        self.lb1.grid(row=0, column=2, sticky="w", pady=5)

        self.lb1 = Label(master=self.window, text="Director", font=self.myfont)
        self.lb1.grid(row=1, column=0, sticky="w", pady=5)

        self.lb1 = Label(master=self.window, text="  Actress / Actor", font=self.myfont)
        self.lb1.grid(row=1, column=2, sticky="w", pady=5)

        #entrytext: a text in which you can put nformation
        self.text_title = StringVar
        self.et1 = Entry(master = self.window, textvariable = self.text_title, font = self.myfont)
        self.et1.grid(row = 0, column = 1, sticky="w")

        self.text_year = StringVar
        self.et2 = Entry(master=self.window, textvariable=self.text_year, font=self.myfont)
        self.et2.grid(row=0, column=3, sticky="w")

        self.text_dir = StringVar
        self.et3 = Entry(master=self.window, textvariable=self.text_dir, font=self.myfont)
        self.et3.grid(row=1, column=1, sticky="w")

        self.text_lead = StringVar
        self.et4 = Entry(master=self.window, textvariable=self.text_lead, font=self.myfont)
        self.et4.grid(row=1, column=3, sticky="w")


        #main screen
        self.listbox = Listbox(master=self.window, font=self.yourfont, height=10, width=80) #height: 10 lines of text inside of it
        self.listbox.grid(row=2, column=0, rowspan=8, columnspan=2, padx=20, pady=40)
        # need to bind an action for clicking in the listbox
        self.listbox.bind("<<ListboxSelect>>", func=self.get_row) #self.getrow is a function that needs to be created.

        self.scroll = Scrollbar(master=self.window)
        self.scroll.grid(row=2, column=2, rowspan=8, sticky="nsw", pady=40)
        #link it to the listbox: it is not yet scrolling into the listbox
        self.scroll.configure(command=self.listbox.yview) #yuscroll?

        #the buttons
        self.bt1 = Button(master=self.window, width=10, text="View All", font=self.myfont, command=self.view)
        self.bt1.grid(row=2, column=3)

        self.bt2 = Button(master=self.window, width=10, text="Delete", font=self.myfont, command=self.delete)
        self.bt2.grid(row=3, column=3)

        self.bt3 = Button(master=self.window, width=10, text="Add", font=self.myfont, command=self.add)
        self.bt3.grid(row=4, column=3)

        self.bt4 = Button(master=self.window, width=10, text="Search", font=self.myfont, command=self.view)
        self.bt4.grid(row=5, column=3)

        self.bt5 = Button(master=self.window, width=10, text="Update", font=self.myfont, command=self.update())
        self.bt5.grid(row=6, column=3)

        self.bt6 = Button(master=self.window, width=10, text="Close", font=self.myfont, command=self.close)
        self.bt6.grid(row=7, column=3)

    def get_row(self, action=None):
        # curselection returns a list of all the selected lines
        if not self.listbox.curselection():
            return
        line_num = self.listbox.curselection()[0]
        idx = self.listbox.get(line_num)[0]
        title = self.listbox.get(line_num)[1]
        year = self.listbox.get(line_num)[2]
        director = self.listbox.get(line_num)[3]
        lead = self.listbox.get(line_num)[4]
        self.text_title.set(title)
        self.text_year.set(year)
        self.text_dir.set(dir)
        self.text_lead.set(lead)

    def view(self):
        data = self.bk.view_all()
        self.listbox.delete(0, END) #END is a constant. a name. When you click again, you dont want to see all the information again. you want to delete the previous.
        for line in data:
            self.listbox.insert(END, line) #keep adding to the END. Each line put it line by line.

    def add(self):#get the information that is going to be inputed into the entry and pass it to the backend, which is going to put it into the DB
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_dir.get()
        lead = self.text_lead.get()
        self.bk.add_element(title, year, director, lead)
        self.view()

    def delete(self):
        #curselection returns a list of all the selected lines
        line_num = self.listbox.curselection() [0]
        idx = self.listbox.get(line_num) [0]
        self.bk.del_element(idx)
        self.view()

    def update(self):
        if not self.listbox.curselection():
            return
        line_num = self.listbox.curselection()[0]
        idx = self.listbox.get(line_num)[0]
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_dir.get()
        lead = self.text_lead.get()
        self.bk.update_element(idx, title, year, director, lead)
        self.view() #display the DB after you updated
        #self.kept_index = self.listbox.get(line_num) [0]


    def close(self): #closes the program
        exit(1)


window = Tk()
Front(window)
window.mainloop()