import sqlite3

# answer
# id | msg | answ
# Добавить несколько запросов ответов

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

# query = """
# CREATE TABLE answer(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     msg TEXT,
#     answ TEXT
# )
# """
# cur.execute(query)
# conn.commit()

# query = """
# INSERT INTO answer(msg,answ) VALUES
# "/start", 'Hello, there are some commands you can use:\n
# 		1) /say [message]\n
# 		2) /myName\n
# 		3) /fish
# """

["id", "answ"]
def get(table_name, cols = "*"):
	db = sqlite3.connect('db.sqlite')
	cur = db.cursor()

	"".format()

	query = """
		SELECT {1} FROM {0}
	""".format(table_name, cols if cols == "*" else "({0})".format(",".join(cols)))

	cur.execute(query)

	colNames = list(map(lambda x: x[0], cur.description))

	result = []
	for i in cur.fetchall():
		result.append(dict(zip(colNames, i)))
	db.close()

	return result

def insert(table_name, cols, data):
	db = sqlite3.connect('db.sqlite')
	cur = db.cursor()

	query = """
	UNSERT INTO {0}({1})
	VALUES('{2}');
	""".format(table_name, ",".join(cols), "','".join(data))

	cur.execute(query)

connect = sqlite3.connect('db.sqlite')
cursor = connect.cursor()

query = """
CREATE TABLE groups(
    id INT PRIMARY KEY AUTOINCREMENT,
    groupName TEXT
)
"""

query = """
CREATE TABLE user(
    id INT PRIMARY KEY,
    FOREIGN KEY group_id REFERENCES groups id
)
"""

cursor.execute(query)
connect.commit()

print(query)
db.commit()
db.close()