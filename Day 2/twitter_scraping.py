import tweepy

consumer_key = 'XOANlh46iHzOLpYrwOL45xP9w'
consumer_secret = '1tqbkg19Qa1xc127eyQ5oUJ1Teodo2CkvX2JYHvGZn1zUieZ7P'
access_token = '214906456-lhVmvjuIqtclbOtoT0fBeU1iB6IztyoSZP4LOJf7'
access_token_secret = "r8mnZtu6foJSyFixkPFIoVUfaQAdeoAHKZDQyp8oDr8ig"


#function to authenticate to Twitter
def connect():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try: 
        api.verify_credentials()
        print("Authentication OK")
        
    except:
        print("Error during authentication")

connect()