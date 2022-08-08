import tweepy
auth = tweepy.OAuth1UserHandler("api_key", "api_key_secret",
                "access_token", "access_token_secret")

client = tweepy.API(auth)

for outputdict1 in tweepy.Cursor(client.search_tweets,q=['#LalSinghChadda']).items():
    dict2=outputdict1._json
    if (dict2['user']['followers_count'] > 300 and dict2['retweet_count']>300):
        print (f"text: {dict2['text']}  ||  tweeted_at: {dict2['created_at']}  ||  link: {dict2['user']['url']}  ||  retweeted: {dict2['retweet_count']} times  ||  likes: {dict2['retweeted_status']['favorite_count']}")
        print ()  
