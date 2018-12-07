from Database import MyDatabase
from time import gmtime, strftime
db = MyDatabase()
try:
# 	value = ""
	time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
# 	for char in time:
# 		value = value + char
# 	print(type(value))
# 	# ID = db.add_user(value)
# 	# print(ID)
# 	db.update_user(1, time)
	
	# db.add_images(1, 'BUtweets', 200)
	ID = 2
	label = 'automotive'
	handle = 'porsche'
	check = db.check_user(ID)
	print(check)

	print(db.update_user(ID,time))
	db.add_label(ID, handle, label)
except Exception as e:
	print(e)

