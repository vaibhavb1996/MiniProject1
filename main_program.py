import tweetscanner
import downimg

from tweetscanner import mediaURLs

def main():
	print("Welcome to my project, Let's get started..")
	tweetscanner.get_all_tweets(input("Enter the twitter handle: "))
	print("Let's get the images..")
	downimg.download_images(mediaURLs)
	print("Images downloaded. Converting to video..")

if __name__=='__main__':
	main()
