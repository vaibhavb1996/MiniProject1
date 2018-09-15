import os, sys
import wget

def download_images(mediaURLs):
	folder=os.getcwd()+"/images"
	try:
		if os.path.exists(folder):
			print("folder already exists")
		else:
			os.mkdir(folder)
	except OSError:
		print("error creating directory")
	#downloading files
	for index,mediaURL in enumerate(mediaURLs):
            img_no=str(index).zfill(3)
            img_name=folder+"/"+img_no+".jpg"
            wget.download(mediaURL, out=img_name)

if __name__=='__main__':
	print("Need main function to call..")
	exit()