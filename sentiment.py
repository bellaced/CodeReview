# twitterexaqmple.py
# Demonstrates connecting to the twitter API and accessing the twitter stream
# Author: Michael Fahy
# ID: 14508
# Email: fahy@chapman.edu
# Course: CPSC 353-01
# Assignment: PA01 Sentiment Analysis
# Version 1.1
# Date: February 15, 2016

# Demonstrates connecting to the twitter API and accessing the twitter stream

import json
import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'eeRdgUPe87uZVylgcqytGp94L'
CONSUMER_SECRET = 'NZHzdWm2yfT2pzKjCs5OBg6tslrN3Icdxh8PPDnfeYxuE5zhqN'
OAUTH_TOKEN = '2525992574-YWvwO8S0AIu4Vhtm9SfdLbhxgVM3CO2Mq2HHFxf'
OAUTH_TOKEN_SECRET = 'xOdjnSJG0idMPbkFQAPkpDFlpEZ1OFxXcvAmXWbxUX3ZP'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Import unquote to prevent url encoding errors in next_results
from urllib import unquote

# XXX: Set this variable to a trending topic,
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.


q = raw_input('Enter a search term: ')



count = 1000


search_results = twitter_api.search.tweets(q=q, count=count)


statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print "Length of statuses", len(statuses)

    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
print json.dumps(statuses[0], indent=1)

print "---------------------------------------------------------------------"
print ' Extracting text, screen names, and hashtags from tweets'
status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]

# Explore the first 5 items for each...

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)




print "---------------------------------------------------------------------"
print 'Sentiment Analysis Results'
sent_file = open('AFINN-111.txt')

scores = {} # initialize an empty dictionary
for line in sent_file:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.

score = 0
for word in words:
    uword = word.encode('utf-8')
    if uword in scores.keys():
        score = score + scores[word]
print float(score)



s = raw_input('Enter Second Search: ')

print s
q = s

search_again = twitter_api.search.tweets(q=q, count=count)


statuses_again = search_again['statuses']

for _ in range(5):
    print "Length of statuses", len(statuses_again)
    try:
        next_results = search_again['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_again = twitter_api.search.tweets(**kwargs)
    statuses_again += search_again['statuses']

# Show one sample search result by slicing the list...
print json.dumps(statuses_again[0], indent=1)

status_texts = [ status['text']
                 for status in statuses_again ]

screen_names = [ user_mention['screen_name']
                 for status in statuses_again
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses_again
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]

# Explore the first 5 items for each...

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)


print "---------------------------------------------------------------------"
print 'Sentiment Analysis on second search'

sent_file = open('AFINN-111.txt')

scores = {} # initialize an empty dictionary
for line in sent_file:
    term, score2  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score2)  # Convert the score to an integer.

score2 = 0
for word in words:
    uword = word.encode('utf-8')
    if uword in scores.keys():
        score2 = score2 + scores[word]
print float(score2)

print '---------------------------------------------'

print 'Comparison on Search Terms'

if score > score2:
  print('Score 1 was more positive')
else:
  print('Score 2 was more positive')

