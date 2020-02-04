import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="localhost", user="erizho21", passwd="zhou", db="erizho21")
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
sql = "UPDATE students SET gradeLevel='12' WHERE id=3"
#Cursor executing sql code
cur.execute(sql)
#Disconnecting cursor and database
cur.close()
db.close()
