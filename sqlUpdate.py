import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="localhost", user="api", passwd="f103", db="people")
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
sql = "UPDATE students SET gradeLevel='12' WHERE id=3"
#Cursor executing sql code
cur.execute(sql)
db.commit()
#Disconnecting cursor and database
cur.close()
db.close()
