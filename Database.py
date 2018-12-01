import mysql.connector

class MyDatabase():
	def __init__(self): #2 tab shifts afterwards
		self.db = mysql.connector.connect(
						host = "localhost",
						user = "root",
						password = "bu",
						database = "TweetDatabase"
									)

		db = mysql.connector.connect(
						host = "localhost",
						user = "root",
						password = "bu",
						database = "TweetDatabase"
									)
		# self.cursor = self.db.cursor()
		cursor = db.cursor()

		# cursor.execute("CREATE DATABASE TweetDatabase") !Has to be used just once!
		# cursor.execute("CREATE TABLE Tweethistory(UserID INT, LastUsed DATETIME)") #The main table for the data !Only called once!
		# cursor.execute("CREATE TABLE Tags(UserID INT, Handle VARCHAR(20), Tag VARCHAR(20))") #Relational table that will contain all the tags generated along with the UserID that encountered them !Only called onec!
		# cursor.execute("CREATE TABLE Images(UserID INT, Handle VARCHAR(20), Img INT)") #Relational table that will have the images related to each twitter handle 
		# cursor.execute("""ALTER TABLE Tweethistory
				#		  ADD PRIMARY KEY (UserID)""") #!Added Primary Key to the Tweethistory table
		# cursor.execute("SHOW TABLES") #!Testing if it worked!
		# for x in cursor:
		# 	print(x)
