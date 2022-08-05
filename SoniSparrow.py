

import tweepy
# current authentication Handler- OAuth 1.0a User Context authentication Hanadler
class Tweets:
    def __init__(self,username):
        self.username=username
    
    def Tweets(self):
        auth = tweepy.OAuth1UserHandler(
            "api_key", "api_key_secret",
            "access_token", "access_token_secret"
        )
        #api v1.1 ka client
        client = tweepy.API(auth)
        def Finduserid(username):
        try:
            userid=client.get_user(screen_name=f"{username}")
            dict1=userid._json
            return (dict1['id'])

        except Exception as err:
            return (err)

    username=input("username(screen_name): ")
    userid=Finduserid(username)
    print (userid)
    #api v2 client
    clientv2=tweepy.Client(bearer_token='bearer_token')
    try:
        #tweets=clientv2.get_users_tweets(id=f'{userid}',place_fields={'country' :'Taiwan'})
        index=1
        for tweets in tweepy.Paginator(clientv2.get_users_tweets,id=f'{userid}'):
            tweetdata=tweets[0]
            for tweet in tweetdata:
                print (f"{index} | {tweet.id} | {tweet.text}")
                index+=1
    except Exception as err:
        print (err)



#Hindustaan times= 36327407
#The Hindu= 36327407
#The Times of India= 134758540
