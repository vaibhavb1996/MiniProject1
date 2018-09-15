import tweetscanner

def main():
	print("Welcome to my project, Let's get started..")
	tweetscanner.get_all_tweets(input("Enter the twitter handle: "))
	print("Images downloaded. Converting to video..")
	

if __name__=='__main__':
	main()
