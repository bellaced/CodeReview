#Sentinment.py
#Andre Perkins
#Demonstrates connecting to twitter API

import json
import twitter

CONSUMER_KEY = 'eeRdgUPe87uZVylgcqytGp94L'
CONSUMER_SECRET = 'NZHzdWm2yfT2pzKjCs5OBg6tslrN3Icdxh8PPDnfeYxuE5zhqN'
OAUTH_TOKEN = '2525992574-YWvwO8S0AIu4Vhtm9SfdLbhxgVM3CO2Mq2HHFxf'
OAUTH_TOKEN_SECRET = 'xOdjnSJG0idMPbkFQAPkpDFlpEZ1OFxXcvAmXWbxUX3ZP'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Import unquote to prevent url encoding errors in next_results
from urllib import unquote

counter = 0
search_scores = []

while counter !=2:
  counter += 1
  q = raw_input('Enter Search Term: ')
  count = 1000
  
  search_results = twitter_api.search.tweets(q=q, count=count)

  statuses = search_results['statuses']

  for _ in range(5):
     print "Getting search terms...Length of statuses", len(statuses)
     try:
        next_results = search_results['search_metadata']['next_results']
     except KeyError, e: # No more results when next_results doesn't exist
        break

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


  print json.dumps(status_texts[0:5], indent=1)
  print json.dumps(screen_names[0:5], indent=1)
  print json.dumps(hashtags[0:5], indent=1)
  print json.dumps(words[0:5], indent=1)



  print "---------------------------------------------------------------------"
  print ' Sentiment Analysis on search terms'
  sent_file = open('AFINN-111.txt')

  scores = {} # initialize an empty dictionary
  for line in sent_file:
    term, score  = line.split("\t") 
    scores[term] = int(score)  # Convert the score to an integer.

  score = 0
  for word in words:
    uword = word.encode('utf-8')
    if uword in scores.keys():
        score = score + scores[word]
  search_scores.append(score)

print ('Search Score of first term')          
print float(search_scores[0])

print ('\n---------------------')

print('Search Score of second term')
print float(search_scores[1])

print '\n--------------------------------'
print 'Comparison\n'

if search_scores[0] > search_scores[-1]:
  print float(search_scores[0])
  print('First Search term was more positive')
  
else:
  print('Second Search term was more positive')
  print float(search_scores[1])


