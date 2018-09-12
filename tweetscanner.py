#!/usr/bin/env python
#author: Vaibhav Bansal

#importing twitter and json modules
import tweepy as twi
import json 

#Twitter Credentials
consumerKey="Enter your consumer key"
consumerSecret="Enter your consumer secret"
accessKey="Enter your access keys"
accessSecret="Enter your access secret"

#verifying credentials
print(twi.Api.VerifyCredentials())

