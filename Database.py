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

	def close_connection(self):
		self.db.disconnect()

	# def user(self):
	# 	self.cursor.execute("""
	# 		SELECT * FROM Tweethistory""")
	# 	return self.cursor.lastrowid

	def get_all_data(self, ID):
		self.cursor.execute("""
			SELECT * FROM Tweethistory""")
		result0 = self.cursor.fetchall()
		for x in result:
			print(x)
		self.cursor.execute("""
			SELECT * FROM Images""")
		result1 = self.cursor.fetchall()
		for x in result:
			print(x)
		self.cursor.execute("""
			SELECT * FROM Tags""")
		result2 = self.cursor.fetchall()
		for x in result:
			print(x)

	def get_all_handles(self):
		self.cursor.execute("""
			SELECT * FROM Tags""")
		result = self.cursor.fetchall()
		handles = []
		for x in result:
			if x[1] in handles:
				pass
			else:
				handles.append(x[2])
		print(handles)

	def get_all_tags(self):
		self.cursor.execute("""
			SELECT * FROM Tags""")
		result = self.cursor.fetchall()
		tags = []
		for x in result:
			if x[2] in tags:
				pass
			else:
				tags.append(x[2])
		print(tags)

	def avg_images(self):
		self.cursor.execute("""
			SELECT * FROM Images""")
		result = self.cursor.fetchall()
		images = 0
		for x in result:
			images += x[2]
		print("Avg images per session: {}".format(images/len(result)))

	def add_user(self, time):
		self.cursor.execute("""
			INSERT INTO Tweethistory (LastUsed)
			VALUES (%s)
			""", (time,))
		self.db.commit()
		user = self.cursor.lastrowid
		return user

	def add_images(self, ID, handle, images):
		self.cursor.execute("""
			INSERT INTO Images (UserID, Handle, Img)
			VALUES (%s, %s, %s)
			""", (ID, handle, images))
		self.db.commit()

	# def update_images(self, ID, handle, images):
	# 	self.cursor.execute("""
	# 		UPDATE Images
	# 		SET Handle = '%s'
	# 		WHERE UserID = %s
	# 		""", (handle, ID))
	# 	self.db.commit()
	# 	self.cursor.execute("""
	# 		UPDATE Images
	# 		SET Img = %s
	# 		WHERE UserID = %s
	# 		""",(images, ID))
	# 	self.db.commit()


	def update_user(self, ID, time):
		try:
			self.cursor.execute("""
				UPDATE Tweethistory
				SET LastUsed = %s
				WHERE UserID = %s
				""", (time, int(ID)))
			self.db.commit()
			
		except:
			return "Problem occurred!" 


	def add_label(self, ID, handle, label):
		self.cursor.execute("""
			INSERT INTO Tags (UserID, Handle, Tag)
			VALUES (%s, %s, %s)
			""", (ID, handle, label))
		self.db.commit()

	def check_user(self, ID):
		self.cursor.execute("""
			SELECT 1
			FROM Tweethistory
			WHERE UserID = %s
			""",(ID,))
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
