#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import time

#Twitter API credenciales
consumer_key = 'ckCAdVpxuzGhmZXtht6ZJNq9D'
consumer_secret = 'QI5vXnStxZ8IvVg2nFl6ax9wmmhStAp8YOxWsUZZEX4zxfmIpP'
access_key = '814169077589639168-FC2RBNkypmRrkmGMAFMMtxc3ir7PpoS'
access_secret = '1sQ2mrFVBWR2v677IsZvH5GRms2aICkztb831fT51bQiU'

def search_by_word(search_word, last_tweet):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    users = tweepy.Cursor(api.search,q = search_word).items()
    count = 0
    errorCount=0
    primero = 0

    #Cambiar a search_word.json (si el nombre ya esta usado que cambie a )
    file = open('search.json', 'wb')
    str_id = last_tweet

    while True:
        try:
            user = next(users)

            #Limite de twitts
            #if (count>10):
            #    break
        except tweepy.TweepError:
            #Atrapa un error, pausa el program, y renicia despues de 15 minutos
            print "sleeping...."
            time.sleep(60*15)
            user = next(users)
        except StopIteration:
            break
        try:
            #Borrar print
            print "Escribiendo tweet:"
            if (user.id == str_id):
                break

            count += 1
            if(primero == 0 and str_id == -1):
                str_id = user.id
                primero = 1

            print user.id

            json.dump(user._json,file,sort_keys = True,indent = 4)

        except UnicodeEncodeError:
            errorCount += 1
            print "UnicodeEncodeError,errorCount ="+str(errorCount)

    print "completed, errorCount ="+str(errorCount)+" total tweets="+str(count)
    print str_id
    print "Nuevos tweets "+str(count)
    return str_id