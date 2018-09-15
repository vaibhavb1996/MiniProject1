#!/usr/bin/env python
#author: Vaibhav Bansal

#importing twitter and json modules
import tweepy 
import json 

#Twitter Credentials
#consumerKey="Enter your consumer key"
#consumerSecret="Enter your consumer secret"
#accessKey="Enter your access keys"
#accessSecret="Enter your access secret"

#access twitter credentials from external file
import twicred

def get_all_tweets(screen_name):
	#verifying credentials
	auth=tweepy.OAuthHandler(twicred.consumerKey,twicred.consumerSecret)
	auth.set_access_token(twicred.accessKey,twicred.accessSecret)
	api=tweepy.API(auth)

	#grab tweets
	tweets=[]

	#initial request for new tweets
	newTweets=api.user_timeline(screen_name=screen_name,count=10)

	#save one tweet
	tweets.extend(newTweets)

	#oldest tweet Id
	oldest=tweets[-1].id-1

	#adding more tweets
	while len(tweets)>0:
		#subsequent tweets use oldest's id to avoid duplicacy
		newTweets=api.user_timeline(screen_name=screen_name,count=10,max_id=oldest)
		#add more tweets
		tweets.extend(newTweets)
		
		#update oldest's id
		oldest=tweets[-1].id-1
		#break condition
		if len(tweets)>20:
			break
		print(len(tweets))
	#extracting the image
	mediaURLs=[]
	for i in tweets:
		media=i.entities.get('media',[])
		if len(media)>0:
			url=media[0]['media_url']
			file_type=url.split(".")[-1]
			if file_type=='jpg':
				mediaURLs.append(media[0]['media_url'])

if __name__=='__main__':
	get_all_tweets("@BU_Tweets")