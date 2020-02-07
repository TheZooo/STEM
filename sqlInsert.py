import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="school")
db.autocommit(True)
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
#Variables
nameIn = 'Eric'
ageIn = 16
gradeLevelIn = 11
#Sql command that inserts the variables via f string
sql = f"INSERT INTO students (name, age, gradeLevel) VALUES ('{nameIn}', '{ageIn}', '{gradeLevelIn}')"
#Cursor executing sql code
cur.execute(sql)
#Disconnecting cursor and database
cur.close()
db.close()
