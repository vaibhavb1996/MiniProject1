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

