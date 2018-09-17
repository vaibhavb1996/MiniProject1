import tweetscanner
import make_video
import analysis

def main():
	print("Welcome to my project, Let's get started..")
	handle=input("Enter the twitter handle: ")
	#calling tweetscanner to get tweets
	tweetscanner.get_all_tweets(handle)
	print("Images downloaded. Converting to video..")
	#calling make video to generate video from images
	make_video.create_video(handle)
	print("Analysing video..")
	path=handle+".mp4"
	analysis.ayalyse_video(path)

if __name__=='__main__':
	main()
