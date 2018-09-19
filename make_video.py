#Copyright 2018 Vaibhav Bansal vbansal@bu.edu
import os

def create_video(screen_name):
	print("entered make video")
	try:
		command="ffmpeg -framerate 1 -i images/%05d.jpg -vcodec mpeg4 "+screen_name+".mp4"
		os.system(command)
		print("Video created..")
	except Exception as error:
		print("Error in making video: "+error)
		exit()

if __name__=='__main__':
	print("Not running from main function..")
	create_video(screen_name)
