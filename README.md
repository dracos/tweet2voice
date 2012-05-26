tweet2voice
===========

Pipes someone's tweets to say, so you can pretend they're with you.

This simply passes the text to 'say', the voice command in Mac OS X, or 'flite'
on Ubuntu, so currently only works on them. Patches to work on more systems
welcome!

Copy config.py-example to config.py, and edit to have the names of the people
of interest, and your Twitter login details.

Install tweepy (using pip install -r requirements.txt will do that, preferably
in a virtualenv), then you can just run:

$ python -u tweet2voice.py

I'm using a fork of tweepy that fixes a streaming bug in it.
