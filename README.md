tweet2voice
===========

Pipes someone's tweets to say, so you can pretend they're with you.

This simply passes the text to 'say', the voice command in Mac OS X, so
currently only works on that. Patches to work on more systems welcome!

Copy config.py-example to config.py, stick in your OAuth parameters and the
name of the person of interest, and set it running.

$ python -u tweet2voice.py

PyPi's version of tweepy is working okay, but latest on github appears to have
a bug in its streaming support (a number of issues/pull requests give fixes).
