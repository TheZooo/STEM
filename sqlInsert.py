import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="localhost", user="erizho21", passwd="zhou", db="erizho21")
db.autocommit(True)
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
#Variables
nameIn = 'Eric'
ageIn = 16
gradeLevelIn = 11
#Sql command
sql = f"INSERT INTO students (name, age, gradeLevel) VALUES ('{nameIn}', '{ageIn}', '{gradeLevelIn}')"
#Cursor executing sql code
cur.execute(sql)
#Disconnecting cursor and database
cur.close()
db.close()
