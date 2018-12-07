import pymongo 
from time import gmtime, strftime

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myclient['myDatabase']
Tweethistory = myDB['Tweethistory']

# Tweethistory.drop()
mydict = {'_id': 1,
		  'LastUsed': time,
		  'usage' : [
						{
						'Tags' : ['Metropolitan', 'Cityscape', 'Urban'],
						'Handle' : 'BUTweets',
						'Images' : 100
						},
						{
						'Tags' : ['Dogs', 'Labrador'],
						'Handle' : 'Dogsforlife',
						'Images' : 100
						}
					]
		 }
x = Tweethistory.insert_one(mydict)
print(myclient.list_database_names())
print(myDB.list_collection_names())
for x in Tweethistory.find():
	print(x)

def add_user(data):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	myDB = myclient['myDatabase']
	Tweethistory = myDB['Tweethistory']
	z = Tweethistory.insert_one(data)
	return z.inserted_id

def update_user(ID, LastUsed, session):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	myDB = myclient['myDatabase']
	Tweethistory = myDB['Tweethistory']
	query_1 = {'_id': ID}
	newval_1 = {'$set': {'LastUsed': LastUsed}}
	Tweethistory.update_one(query_1, newval_1)

	query_2 = {'_id': ID}
	newval_2 = {'$push': {'usage': session}}
	Tweethistory.update_one(query_2, newval_2)
	




