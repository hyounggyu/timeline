#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import datetime
from pymongo import MongoClient
import operator

tweets = MongoClient().mytimeline.tweets

today = datetime.datetime.today()
dlist = [ (today - datetime.timedelta(days=x)).strftime("%b %d") for x in range(10) ]

for d in dlist:
  regx = re.compile(r'.*'+d+'.*')
  ts = tweets.find({ "created_at": regx })
  users = {}
  for t in ts:
    if u'user' in t:
      name = t[u'user'][u'screen_name']
      users[name] = users[name] + 1 if name in users else 1
  print d, ts.count()
  print sorted(users.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
