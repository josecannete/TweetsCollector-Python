import tweepy
import json
import os

#Twitter API credentials
consumer_key = 'ckCAdVpxuzGhmZXtht6ZJNq9D'
consumer_secret = 'QI5vXnStxZ8IvVg2nFl6ax9wmmhStAp8YOxWsUZZEX4zxfmIpP'
access_key = '814169077589639168-FC2RBNkypmRrkmGMAFMMtxc3ir7PpoS'
access_secret = '1sQ2mrFVBWR2v677IsZvH5GRms2aICkztb831fT51bQiU'

#Maximo de tweets por busqueda
limite_tweets = 1000

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