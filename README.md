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

PyPi's version of tweepy is working okay, but latest on github appears to have
a bug in its streaming support (a number of issues/pull requests give fixes).
