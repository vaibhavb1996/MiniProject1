from Database import MyDatabase
from time import gmtime, strftime
db = MyDatabase()
try:
	value = ""
	time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	for char in time:
		value = value + char
	print(type(value))
	ID = db.add_user(value)
	print(ID)
	db.add_images(1, 'BUtweets', 200)
except Exception as e:
	print(e)

