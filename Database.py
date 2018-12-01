import mysql.connector
# class MyDatabase:
	# def __init__(self): #2 tab shifts afterwards
# self.db = mysql.connector.connect(
# 				host = "localhost",
# 				user = "root",
# 				password = "bu",
# 				database = "TweetDatabase"
# 							)

db = mysql.connector.connect(
				host = "localhost",
				user = "root",
				password = "bu",
				database = "TweetDatabase"
							)
# self.cursor = self.db.cursor()
cursor = db.cursor()
# cursor.execute("CREATE DATABASE TweetDatabase") !Has to be used just once!
# cursor.execute("CREATE TABLE Tweethistory(UserID INT, LastUsed DATETIME, Handle VARCHAR(30), TotalImages INT)") #The main table for the data
cursor.execute("CREATE TABLE Tags(UserID INT, Tag VARCHAR(20))") #Relational table that will contain all the tags generated along with the UserID that encountered them

# cursor.execute("SHOW DATABASES") !Testing if it worked!
# for x in cursor:
# 	print(x)
