#!/usr/bin/env python

import subprocess
import tweepy
from config import *

api = tweepy.API()

class Listener ( tweepy.StreamListener ):
  def on_status( self, status ):
    if status.author.id not in user_ids:
        return True
    print status.author.screen_name, status.text
    try:
        subprocess.call( [ 'say', status.text ] )
    except OSError:
        try:
            subprocess.call( [ 'flite', status.text ] )
        except OSError:
            pass
    return True

# We need the IDs of the given Twitter user names
# We can also then check if any are protected accounts
users = api.lookup_users( screen_names=PEOPLE_OF_INTEREST )
user_ids = [ user.id for user in users ]
users_protected = [ user for user in users if user.protected ]
if users_protected:
    if not CONSUMER_KEY:
        raise Exception, "You need to use OAuth if you want this to work on a protected account"
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
else:
    auth = tweepy.BasicAuthHandler(USERNAME, PASSWORD)

listener = Listener()
stream = tweepy.Stream( auth=auth, listener=listener )

if users_protected:
    # We want to additionally follow any IDs for non-private people,
    # as well as the user stream
    user_ids_public = [ user.id for user in users if not user.protected ]
    stream.userstream( follow=user_ids_public )
else:
    # We want to follow the IDs of everyone
    stream.filter( follow=user_ids )

