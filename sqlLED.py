import RPi.GPIO as GPIO
import pymysql
import time

#Set GPIO pin 3 as an output
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin = 3
GPIO.setup(ledPin, GPIO.OUT)

def checker():
	#Connect to mysql on pi
	db = pymysql.connect(host="localhost", user="piControl", passwd="f103", db="piLight")
	cur = db.cursor(pymysql.cursors.DictCursor)
	
	#Get the switchLight value from table lightState
	sql = "SELECT switchLight FROM lightState"
	cur.execute(sql)
	row = cur.fetchall()
	
	print(row[0]["switchLight"])
	
	#Checks switchLight value and turns the LED on/off accordingly
	if row[0]["switchLight"] is 0:
		GPIO.output(ledPin, GPIO.LOW)
	elif row[0]["switchLight"] is 1:
		GPIO.output(ledPin, GPIO.HIGH)
		
	cur.close()
	db.close()
	
	#Wait half a second and loops
	time.sleep(0.5)
	checker()
	
checker()
