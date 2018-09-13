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

#save new tweets
tweets.extent(newTweets)