import requests
import json
import re 
import time

#Auth Bearer token
auth_token = ""

#Max Tweets to fetch 
max_tweets = 15000

#Tweets per call (max 100)
tweets_per_call = 100

#Requests per 15 minutes (max 150)
twitter_request_rate = 150

def write_file(file,data):
    f = open(file, "a")
    f.write(data)
    f.close()

def fetchTweets(conversation_id, next_token, count):
    if count==0:
        write_file("tweets_"+conversation_id+".csv", "Index,Id,Comment\n")
    alldata = []
    params = {}
    params['query'] = 'conversation_id:' + conversation_id, 
    params['max_results'] = tweets_per_call
    params["next_token"] = None if next_token is None else next_token
    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['Authorization'] = 'Bearer ' + auth_token
                
    print("Making Request...")
    print(params)
    response = requests.get('https://api.twitter.com/2/tweets/search/recent', params=params, headers=headers).json()
    #print(response)
    next_token=response['meta'].get('next_token')
    for tweet in response['data']:
        txt = tweet['text']
        txt = txt.replace('\n', ' ')
        txt = txt.replace('"', "'")
        txt = re.sub('@elonmusk', '',txt, flags=re.I)
        alldata.append('{},"{}","{}"'.format(count, tweet['id'], txt.strip()))
        count = count + 1
    print("Data Fetched:",  count)
    write_file("tweets_"+conversation_id+".csv", "\n".join(alldata)+"\n")
    
    if count<max_tweets and next_token is not None: 
        delay = 900/twitter_request_rate
        print('Waiting {} seconds before making next call...'.format(delay))
        time.sleep(delay)
        fetchTweets(conversation_id, next_token, count)
    
fetchTweets("1589390597798125568", None, 0)
fetchTweets("1590383937284870145", None, 0)
fetchTweets("1590785323105423360", None, 0)
fetchTweets("1591842546216763399", None, 0)
fetchTweets("1592447141720780803", None, 0)