import mysql.connector

class MyDatabase():
	def __init__(self): #2 tab shifts afterwards
		self.db = mysql.connector.connect(
						host = "localhost",
						user = "root",
						password = "bu",
						database = "TweetDatabase"
									)

		# db = mysql.connector.connect(
		# 				host = "localhost",
		# 				user = "root",
		# 				password = "bu",
		# 				database = "TweetDatabase"
		#							)
		self.cursor = self.db.cursor()
		# cursor = db.cursor()

	def close_connection():
		self.db.disconnect()

	def add_user(self, time):
		self.cursor.execute("""
			INSERT INTO Tweethistory (LastUsed)
			VALUES (%s)
			""",(time))
		self.db.commit()
		return int(self.cursor.lastrowid)

	def add_images(self, ID, handle, images):
		self.cursor.execute("""
			INSERT INTO Images
			VALUES (%d, %s, %d)
			""",(ID, handle, images))
		self.db.commit()
		

	def update_user(self, ID, time):
		self.cursor.execute("""
			UPDATE Tweethistory
			SET LastUsed = %s
			WHERE UserID = %d
			""",(time, ID))
		self.db.commit()


	def add_label(self, ID, handle, label):
		pass

	def check_user(self, ID):
		self.cursor.execute("""
			SELECT 1
			FROM Tweethistory
			WHERE UserID = %d
			"""%(ID))
		if self.cursor.fetchone() == None:
			return False
		else:
			return True

		# cursor.execute("CREATE DATABASE TweetDatabase") !Has to be used just once!
		# cursor.execute("CREATE TABLE Tweethistory(UserID INT, LastUsed DATETIME)") #The main table for the data !Only called once!
		# cursor.execute("CREATE TABLE Tags(UserID INT, Handle VARCHAR(20), Tag VARCHAR(20))") #Relational table that will contain all the tags generated along with the UserID that encountered them !Only called onec!
		# cursor.execute("CREATE TABLE Images(UserID INT, Handle VARCHAR(20), Img INT)") #Relational table that will have the images related to each twitter handle 
		# cursor.execute("""ALTER TABLE Tweethistory
				#		  ADD PRIMARY KEY (UserID)""") #!Added Primary Key to the Tweethistory table
		# cursor.execute("SHOW TABLES") #!Testing if it worked!
		# for x in cursor:
		# 	print(x)
