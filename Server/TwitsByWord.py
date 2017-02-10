import tweepy
import json
import time
import os

#Twitter API credenciales
consumer_key = 'ckCAdVpxuzGhmZXtht6ZJNq9D'
consumer_secret = 'QI5vXnStxZ8IvVg2nFl6ax9wmmhStAp8YOxWsUZZEX4zxfmIpP'
access_key = '814169077589639168-FC2RBNkypmRrkmGMAFMMtxc3ir7PpoS'
access_secret = '1sQ2mrFVBWR2v677IsZvH5GRms2aICkztb831fT51bQiU'

#Maximo de tweets por busqueda
tweet_limit = 1000

def search_by_word(search_word, last_tweet):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    direccion = 'jsonDirectory/'+ search_word + '.json'

    users = tweepy.Cursor(api.search,q = search_word).items()
    count = 0
    errorCount = 0
    primero = 0

    results = []
    aux = []
    if os.path.isfile(direccion):
        with open(direccion, 'rb') as infile:
            aux = json.load(infile)

    file = open(direccion, 'wb')
    str_id = last_tweet

    while True:
        try:
            user = next(users)

        except tweepy.TweepError:
            #Atrapa un error, pausa el program, y renicia despues de 15 minutos
            print("sleeping....")
            time.sleep(60*15)
            user = next(users)

        except StopIteration:
            break

        try:
            #Borrar print
            if (user.id == last_tweet):
                break

            if (primero == 0 and str_id == -1):
                str_id = user.id
                primero = 1

            count += 1
            if(count > tweet_limit):
                count -= 1
                break

            if(count % 100 == 0):
                print("Escribiendo tweet numero "+str(count))

            results.append(user._json)

        except UnicodeEncodeError:
            errorCount += 1
            print ("UnicodeEncodeError,errorCount = "+str(errorCount))

    results = results + aux
    json.dump(results, file, sort_keys=True, indent=4)
    file.close()

    print("Nuevos tweets "+str(count))
    return str_id
