#!/usr/bin/python
# -*- coding:utf-8 -*-

import tweepy, webbrowser

from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url(signin_with_twitter=True)
webbrowser.open(auth_url)
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print auth.access_token.key, auth.access_token.secret
