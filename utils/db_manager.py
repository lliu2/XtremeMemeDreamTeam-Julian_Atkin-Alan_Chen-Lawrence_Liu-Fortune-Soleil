import sqlite3

#need to retrive previous id instead

def userAuth(username, password):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()
     
     if nameAvail(username):
          q = "SELECT * FROM users WHERE username = %s;" % (username)
          users.execute(q)
          info = users.fetchall()
          print info[1]
          if (info[1] == password):
               return True
     return False

def nameAvail(username):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()

     q = "SELECT * FROM users WHERE username=" + '"' + username + '"'
     users.execute(q)
     info = users.fetchall()
     if (len(info) > 0): return False
     else: return True

def addUser(username, password):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()
     
     if nameAvail(username):
          q = "SELECT userid FROM users WHERE userid = (SELECT MAX(userid) FROM users);"
          users.execute(q)
          x = users.fetchall()
          q = "INSERT INTO users VALUES (\"%s\", \"%s\", %s);" % (username, password, x[0])
          users.execute(q)
          return 1;
     else:
          return 0;
    
def addStory(userid, inpt, title):
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()
     
     #timestamp = stuff
     q = "INSERT INTO " + title + " VALUES (\"%s\", %s, %s)" % (timestamp, userid, inpt)
     stories.execute(q)

#def showStuff

