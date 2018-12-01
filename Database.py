import mysql.connector

db = mysql.connector.connect(
					host = "localhost",
					user = "root",
					password = "bu",
					database = "TweetDatabase"
							)
cursor = db.cursor()
# cursor.execute("CREATE DATABASE TweetDatabase") !Has to be used just once!
cursor.execute("CREATE TABLE Tweethistory(UserID INT, LastUsed DATETIME, Handle VARCHAR[30], TotalImages INT")
# cursor.execute("SHOW DATABASES") !Testing if it worked!
# for x in cursor:
# 	print(x)
