import mongo_db as db

def get_all_data(ID):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	myDB = myclient['myDatabase']
	Tweethistory = myDB['Tweethistory']
	for x in Tweethistory.find({'_id': ID}):
		print(x)

def get_all_tags():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	myDB = myclient['myDatabase']
	Tweethistory = myDB['Tweethistory']
	for x in Tweethistory.find({}, {'_id':0, 'LastUsed':0}):
		for mydict in enumerate(x.get('usage')):
			print(mydict.get('Tags'))

def get_all_handles():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	myDB = myclient['myDatabase']
	Tweethistory = myDB['Tweethistory']
	for x in Tweethistory.find({}, {'_id':0, 'LastUsed':0}):
		for mydict in enumerate(x.get('usage')):
			print(mydict.get('Handle'))

def avg_images():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	myDB = myclient['myDatabase']
	Tweethistory = myDB['Tweethistory']
	add = 0
	for x in Tweethistory.find({}, {'_id':0, 'LastUsed':0}):
		for mydict in enumerate(x.get('usage')):
			add += mydict.get('images')
	print("The average is {}".format(add / Tweethistory.find({}, {'_id':0, 'LastUsed':0}).count()))

choice = 0
while choice is not 5:
	print("This program lets you do the following:")
	print("1. Display all data")
	print("2. Display all tags")
	print("3. Display all handles used")
	print("4. Avg no. of images per session")
	print("5. Exit\n")

	choice = int(input("Enter your choice: "))
	if choice is 1:
		ID = input("Enter User ID")
		get_all_data(ID)
	elif choice is 2:
		get_all_tags()
	elif choice is 3:
		get_all_handles()
	elif choice is 4:
		avg_images()
	elif choice is 5:
		print("Thanks for using the program. Ciao!")
		exit()
	else:
		print("Wrong choice, Try again!")

