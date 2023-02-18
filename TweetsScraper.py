import tweepy
# current authentication Handler- OAuth 1.0a User Context authentication Hanadler



def Getuserid(username):
    auth = tweepy.OAuth1UserHandler(
                "api_key", "api_key_secret",
                "access_token", "access_token_secret")
    # api v1.1 ka client
    client = tweepy.API(auth)
    getusrid = client.get_user(screen_name=f"{username}")
    dict1 = getusrid._json
    return dict1['id']




def Gettweets(username):
    userid=Getuserid(username)
    clientv2 = tweepy.Client(
    bearer_token='bearer_token')
    tweetscount = 1
    try:
        for tweets in tweepy.Paginator(clientv2.get_users_tweets, id=f'{userid}'):
            tweetdata = tweets[0]
            for tweet in tweetdata:
                print(f"{tweetscount} | {tweet.id} | {tweet.text}")
                tweetscount += 1
                #if you want to set limit of tweets retriving uncomment the section below and set the integer value according to needs
                #if (tweetscount == integer):
                #    break
            #if (tweetscount == integer):    
            #    break
    except Exception as err:
        print(err)
