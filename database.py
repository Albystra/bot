import sqlite3

# answer
# id | msg | answ
# Добавить несколько запросов ответов

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

query1 = """
CREATE TABLE groups(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	groupName TEXT
	)"""

query2 = """
CREATE TABLE user(
	id INTEGER PRIMARY KEY,
	groupId INTEGER, 
    
    FOREIGN KEY (groupId) REFERENCE groups (id)
	)"""

cur.execute(query1)
db.commit()
cur.execute(query2)
db.commit()

db.close()

insert("groups", ["groupName"], ["Администратор"])
insert("groups", ["groupName"], ["Наставник"])
insert("groups", ["groupName"], ["Ученик"])

print(get("groups"))