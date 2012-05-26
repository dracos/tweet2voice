tweet2voice
===========

Pipes someone's tweets to say, so you can pretend they're with you.

This simply passes the text to 'say', the voice command in Mac OS X, or 'flite'
on Ubuntu, so currently only works on them. Patches to work on more systems
welcome!

Copy config.py-example to config.py, and edit to have the names of the people
of interest, and your Twitter login details (or OAuth parameters if you want
this to work on protected people; you'll need a registered Twitter app).

Install tweepy (using pip install -r requirements.txt will do that, preferably
in a virtualenv), then you can just run:

$ python -u tweet2voice.py

I'm using my own fork of a fork of tweepy that fixes a streaming bug in it, and
adds some functionality to the user stream call.
