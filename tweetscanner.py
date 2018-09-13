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
	print("..%s tweets downloaded so far" %len(tweets))

#write tweets to JSON
file=open('tweets.json', 'w')
print("File being exported to JSON")
for status in tweets:
	json.dump(status._json, file, sort_keys=True, indent=4)

#close file
print("Done")
file.close()

if __name__='__main__':
		get_all_tweets("@BU_Tweets")