#!/usr/bin/env python
#author: Vaibhav Bansal

#importing twitter and json modules
import tweepy 
import os, sys ,wget

#Twitter Credentials
consumerKey="Enter your consumer key"
consumerSecret="Enter your consumer secret"
accessKey="Enter your access keys"
accessSecret="Enter your access secret"

#access twitter credentials from external file
#import twicred

def get_all_tweets(screen_name):
	#verifying credentials
	auth=tweepy.OAuthHandler(twicred.consumerKey,twicred.consumerSecret)
	auth.set_access_token(twicred.accessKey,twicred.accessSecret)
	api=tweepy.API(auth)
	#twitter handle confirmation
	try:
		user=api.get_user(screen_name)
		print(user.id_str)
		print(user.screen_name+" exists")
	except:
		print("username doesn't exist. Try running with another username.\n ")
		get_all_tweets(input("Enter Twitter Handle: "))
	#grab tweets
	tweets=[]

	#initial request for new tweets
	newTweets=api.user_timeline(screen_name=screen_name,count=1)

	#save one tweet
	tweets.extend(newTweets)

	#oldest tweet Id
	oldest=tweets[-1].id-1
	i=1
	count=[len(tweets)]
	#adding more tweets
	while i>0:
		#subsequent tweets use oldest's id to avoid duplicacy
		newTweets=api.user_timeline(screen_name=screen_name,count=200,max_id=oldest)
		#add more tweets
		tweets.extend(newTweets)
		
		#update oldest's id
		oldest=tweets[-1].id-1
		count.append(len(tweets))

		#break condition
		if len(tweets)>2000 or count[i]==count[i-1]:
			break
		i=i+1
		print(len(tweets))
	
	#extracting the image URLs
	mediaURLs=[]
	for i in tweets:
		media=i.entities.get('media',[])
		if len(media)>0:
			url=media[0]['media_url']
			file_type=url.split(".")[-1]
			if file_type=='jpg':
				mediaURLs.append(media[0]['media_url'])
	
	#no images exception
	if len(mediaURLs)==0:
		print("no images to download, try another twitter handle")
		get_all_tweets(input("Enter Twitter handle: "))
	
	folder=os.getcwd()+"/images"
	try:
		if os.path.exists(folder):
			print("folder already exists")
		else:
			os.mkdir(folder)
	except OSError:
		print("error creating directory")
	
	#downloading files
	print("Let's get the images..")
	for index,mediaURL in enumerate(mediaURLs):
            img_no=str(index).zfill(5)
            img_name=folder+"/"+img_no+".jpg"
            wget.download(mediaURL, out=img_name)


if __name__=='__main__':
	print("Not running from main program..")
	get_all_tweets(input("Enter the twitter handle: "))