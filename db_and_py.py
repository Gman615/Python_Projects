import sqlite3


conn = sqlite3.connect('RAM.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Roster( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            Name TEXT, \
            Species TEXT, \
            IQ INT)")            
    conn.commit()
conn.close()


conn = sqlite3.connect('RAM.db')

with conn:
    cur = conn.cursor()
    cur.execute("UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'")
    conn.commit()
conn.close()

conn = sqlite3.connect('RAM.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
myresult = cur.fetchall()

for x in myresult:
    print(x)


    

    
