#!/usr/bin/env python

import os
import tweepy
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class Listener ( tweepy.StreamListener ):
  def on_status( self, status ):
    print status.author.screen_name, status.text
    if status.author.screen_name == PERSON_OF_INTEREST:
        os.system('say "' + status.text.replace('"', r'\"') + '"')
    return True

listener = Listener()
stream = tweepy.Stream( auth=auth, listener=listener )
stream.userstream()

