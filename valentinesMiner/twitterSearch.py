# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:48:04 2017

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

with open("tweets3.json", "a") as f:
    for tweet in tweepy.Cursor(api.search, q="#MyLoveLifeIn5Words", lang="en").items():
        try:
            f.write(tweet)
        except Exception:
            pass
    
    f.close()

print("crawl complete")

