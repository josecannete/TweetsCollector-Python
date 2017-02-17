import tweepy
import json
import os

#Twitter API credentials
consumer_key = '9dI0BvlBlBmQjMB7NdeafUpVK'
consumer_secret = 'QG3HjzpQ52FgC5lDc7lg2nCX4fiMHzbqAZ1HclYuJ10MXlBWN0'
access_key = '105785165-8OcCHCUPkz7uDEaLNJrM771Itv9UBFVHKP104biU'
access_secret = '1Ei0vmDVIOQqifjQAri3wLEqD0T0fU0SgmMXAiA6XWnoj'

#Maximo de tweets por busqueda
limite_tweets = 100000000

def search_by_user(screen_name, ultimo):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    direccion = 'usersTweets/' + screen_name + '.json'

    aux = []
    if os.path.isfile(direccion):
        with open(direccion, 'rb') as infile:
            aux = json.load(infile)

    alltweets = api.user_timeline(screen_name = screen_name,count=1000)
    first = alltweets[0].id

    i = 0
    results = []
    while i < len(alltweets):
        if alltweets[i].id == ultimo:
            break
        results.append(alltweets[i]._json)
        i += 1
        if(i%10 == 0):
            print (i)

    results = results + aux

    print ("Escribiendo " + str(i) + " nuevos tweets")

    file = open(direccion, 'wb')
    json.dump(results, file, sort_keys = True, indent = 4)

    print ("Listo")
    file.close()

    return first
