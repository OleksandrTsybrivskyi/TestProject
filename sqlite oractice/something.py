import sqlite3

db=sqlite3.connect('sqlite oractice\itprogger.db')
c=db.cursor()

# c.execute("""CREATE TABLE articles (
#           title text,
#           full_txt text,
#           views integer,
#           avtor text         
# )""")

# c.execute("INSERT INTO articles VALUES ('Amazon','Amazon is cool', 10000,'Jeff Bezos')")

# c.execute("DELETE FROM articles WHERE rowid>2")

c.execute("UPDATE articles SET avtor = 'Admin', views = 100000 WHERE title = 'Google' AND rowid=2")

c.execute("SELECT rowid, * FROM articles WHERE rowid<5 ORDER BY views")
items=c.fetchall()
for el in items:
    print(el)



# print(c.fetchmany(1))
# print(c.fetchone()[1])
db.commit()
db.close()
