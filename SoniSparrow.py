

import tweepy
# current authentication Handler- OAuth 1.0a User Context authentication Hanadler


class GetTweets:
    def __init__(self, username):
        self.username = username

    def Tweets(self):
        try:
            auth = tweepy.OAuth1UserHandler(
                "api_key", "api_key_secret",
                "access_token", "access_token_secret")
            # api v1.1 ka client
            client = tweepy.API(auth)
            getusrid = client.get_user(screen_name=f"{self.username}")
            dict1 = getusrid._json
            userid = dict1['id']

            # api v2 client
            clientv2 = tweepy.Client(
            bearer_token='bearer_token')
            index = 1
            for tweets in tweepy.Paginator(clientv2.get_users_tweets, id=f'{userid}'):
                tweetdata = tweets[0]
                for tweet in tweetdata:
                    print(f"{index} | {tweet.id} | {tweet.text}")
                    index += 1
                    if (index == 50):
                        break
                break
        except Exception as err:
            print(err)


Hindustaan = GetTweets('htTweets')
Hindustaan.Tweets()
print ()
print ()
Hindu = GetTweets('the_hindu')
Hindu.Tweets()
print ()
print ()
Timesofindia = GetTweets('timesofindia')
Timesofindia.Tweets()


# Hindustaan times= 36327407
# The Hindu= 36327407
# The Times of India= 134758540
