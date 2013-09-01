#!/usr/bin/python
# -*- coding:utf-8 -*-
import pprint, re, json
from datetime import datetime
from pymongo import MongoClient

tweets = MongoClient().mytimeline.tweets
pp = pprint.PrettyPrinter(indent=4)

ts = tweets.find(limit=200)
for t in ts:
    pp.pprint(t) 
