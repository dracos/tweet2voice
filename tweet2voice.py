#!/usr/bin/env python

import subprocess
import tweepy
from config import *

auth = tweepy.BasicAuthHandler(USERNAME, PASSWORD)
api = tweepy.API()

class Listener ( tweepy.StreamListener ):
  def on_status( self, status ):
    print status.author.screen_name, status.text
    try:
        subprocess.call( [ 'say', status.text ] )
    except OSError:
        try:
            subprocess.call( [ 'flite', status.text ] )
        except OSError:
            pass
    return True

listener = Listener()
stream = tweepy.Stream( auth=auth, listener=listener )

user_ids = [ x.id for x in api.lookup_users( screen_names=PEOPLE_OF_INTEREST ) ]
stream.filter( follow=user_ids )

