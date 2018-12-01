import tweetscanner
import make_video
import analysis
from Database import MyDatabase
from time import gmtime, strftime

def main():
	db = MyDatabase()
	time = strftime("%Y%m%d %H:%M:%S %p", gmtime())
	print("Welcome to my project, Let's get started..")
	print("\nPlease slect one of the following options:")
	print("1. Use existing ID")
	print("2. Create new ID")

	choice = input("Please enter your choice: ")
	if (choice == 1):
		ID = input("Enter your ID: ")
		check = db.check_user(ID)
		if (check == False):
			print("Wrong ID, Please try again!")
			db.close_connection()
			main()
		else:
			db.update_user(ID, time)
	elif (choice == 2):
		ID = db.add_user(ID, time) #Create new database entry
	else:
		print("Wrong choice, please try again!")
		db.close_connection()
		main()

	handle = input("Enter the twitter handle: ")
	#calling tweetscanner to get tweets
	tweetscanner.get_all_tweets(handle, ID)
	print("Images downloaded. Converting to video..")
	#calling make video to generate video from images
	make_video.create_video(handle)
	print("Analysing video..")
	path = handle + ".mp4"
	analysis.analyse_video(path, ID, handle)
	#closing notes
	db.close_connection()
	print("Thanks for using our application!")

if __name__ == '__main__':
	main()
