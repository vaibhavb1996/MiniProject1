import tweetscanner
import downimg

def main():
	print("Welcome to my project, Let's get started..")
	tweetscanner.get_all_tweets(input("Enter the twitter handle: "))
	print("Let's get the images..")
	downimg.download_images(tweetscanner.mediaURLs)
	print("Images downloaded. Converting to video..")

