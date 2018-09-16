import os

def create_video(screen_name):
	print("entered make video")
	try:
		command="ffmpeg -framerate 1 -i images/%05d.jpg -vcodec mpeg4 "+screen_name+".mp4"
		os.system(command)
		print("Video created..")
	except Exception as e:
		print(e)
		exit()

if __name__=='__main__':
	print("call from main function..")
	#exit()
	create_video(screen_name)