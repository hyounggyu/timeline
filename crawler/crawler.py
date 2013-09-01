#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import json
import logging

import tweepy
from pymongo import Connection

from config import *
from daemon import Daemon

class CustomStreamListener(tweepy.StreamListener):
	def __init__(self):
		self.tweets = Connection().mytimeline.tweets
		super(CustomStreamListener, self).__init__()

	def on_data(self, data):
		self.tweets.insert(json.loads(data))

class CrawlerDaemon(Daemon):
	def __init__(self, *args, **kwargs):
		logging.basicConfig(filename=LOGFILE, format='%(asctime)s %(levelname)s %(message)s', level=logging.WARNING)
		super(CrawlerDaemon, self).__init__(*args, **kwargs)

	def run(self):
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

		while True:
			try:
				streaming_api.userstream()
			except Exception, e:
				logging.error(str(e))
			time.sleep(60)

if __name__ == '__main__':
	import sys

	daemon = CrawlerDaemon(PIDFILE)

	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
