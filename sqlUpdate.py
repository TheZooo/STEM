import MySQLdb
#Connecting to database with mysqldb
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="school")
#Creating cursor
cur = db.cursor(MySQLdb.cursors.DictCursor)
#Cursor executing sql code and commiting
sql = "UPDATE students SET age='17' WHERE name='Eric' AND age=16"
cur.execute(sql)
db.commit()
#Disconnecting cursor and database
cur.close()
db.close()
