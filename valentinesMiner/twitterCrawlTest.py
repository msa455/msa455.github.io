# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:21:48 2017

@author: Main Character
"""

import tweepy 
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json


consumer_key = "lia2iGxNIzL7mQyLREFcJZvgy"
consumer_secret = "LNoWGeAwGlHUo91q1VXtLBUHEkVlIXJeeq6CdJHEFO7FNc4mWa"
access_token = "831141872202502144-q4zwpdhvD26PiDspf2l65GeYLdkn9GC"
access_secret = "7dQd6Rb22xzvdT8t784tJeGN7aEnjFOixamEKwHeOL3zN"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process(tweet):
    print(json.dumps(tweet))

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweets2.json', 'a') as f:
                print(data)
                f.write(data)
                return True
        except BaseException as e:
            print(str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#IfIWereWireTapped'])

    

