import tweetscanner
import make_video
import analysis
import mongo_db as db
from time import gmtime, strftime

def main():
	images = 0
	handle = ''
	time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	# time = "2018-12-02 00:03:10" 
	# a =(str(time))
	# print(type(time))
	print("Welcome to my project, Let's get started..")
	print("\nPlease slect one of the following options:")
	print("1. Use existing ID")
	print("2. Create new ID")

	choice = int(input("Please enter your choice: "))
	if (choice == 1):
		ID = int(input("Enter your ID: "))
		check = db.check_user(ID)
		if (check == 0):
			print("Wrong ID, Please try again!")
			main()
		else:
			pass
	elif (choice == 2):
		ID = int(db.add_user(time))
		print("Your ID is {}".format(ID)) #Create new database entry
	else:
		print("Wrong choice, please try again!")
		main()

	handle = input("Enter the twitter handle: ")
	#calling tweetscanner to get tweets
	images = tweetscanner.get_all_tweets(handle, ID)
	print("Images downloaded. Converting to video..")
	#calling make video to generate video from images
	make_video.create_video(handle)
	print("Analysing video..")
	path = handle + ".mp4"
	Tags = analysis.analyse_video(path, ID, handle)
	#closing notes
	data = {
			'Tags': Tags,
			'Handle': handle,
			'Images': images
		   }
	if choice == 1:
		db.add_usage(ID, data)
	elif choice == 2:
		db.update_user(ID, time, data)

	print("Thanks for using our application!")

if __name__ == '__main__':
	main()
