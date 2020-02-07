import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="localhost", user="erizho21", passwd="password", db="school")
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
sql = "UPDATE students SET age='17' WHERE id=2"
#Cursor executing sql code
cur.execute(sql)
db.commit()
#Disconnecting cursor and database
cur.close()
db.close()
