import sqlite3

class Back(object):
    def __init__(self):
        #create a DB:
        db = sqlite3.connect("movies.db")
        cur = db.cursor() #cursor object to interact with the DB. The one in charge of sending the querries.
        cur.execute("CREATE TABLE IF NOT EXISTS movie(id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, leade TEXT)")
        db.commit()
        db.close()

    def view_all(selfs):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute(
            "SELECT * From movie")
        data = cur.fetchall() #because you are not changing the DB. Only selecting from it. No need of commit because you are not updating or adding informatin to the DB.
        db.close()
        return data #the back end returns a list of all the movies to the front end

    def add_element(self, id, title="", year=2019, director="", lead=""):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("INSERT INTO movie VALUES(NULL, ?, ?, ?, ?)", (title, year, director, lead))
        db.commit()
        db.close()

    def del_element(self, id):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("DELETE FROM movie WHERE id=?", (id,))
        db.commit()
        db.close()

    def update_element(self, id, title="", year=2019, director="", lead=""):
        db = sqlite3.connect("movies.db")
        cur = db.cursor("UPDATE movie SET title=?, year=?, director=?, lead=? WHERE id=?", (title, year, director, lead))
        cur.execute()
        db.commit()
        db.close()




#debug database to see if you have the basic DB functions. Testing it out.
if __name__=="__main__":
    bk = Back()
    db = sqlite3.connect("movies.db")
    cur = db.cursor()
    cur.execute("INSERT INTO movie VALUES(NULL, ?, ?, ?, ?)", ("Finding Neverland", 2007, "Andrew Stanton", "Johny Depp"))
    db.commit()
    cur.execute("SELECT * FROM movie")
    data = cur.fetchall()
    for line in data:
        print(line)
    db.close()