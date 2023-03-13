import tweepy
import pandas as pd

class TwitterScraper:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
    
    def search_tweets(self, query, max_tweets=500):
        tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'Urls'])
        for tweet in tweepy.Cursor(self.api.search_tweets, tweet_mode='extended', q=query, lang="en").items(max_tweets):
            appending_dataframe = pd.DataFrame(
                [[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'), tweet.entities['urls']]],
                columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'Urls'])
            tweet_dataset = tweet_dataset.append(appending_dataframe)
        return tweet_dataset

if __name__ == '__main__':
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    
    scraper = TwitterScraper(consumer_key, consumer_secret, access_token, access_token_secret)
    
    # Define your search queries
    Facebook = "Facebook"
    Apple = "Apple"
    Amazon = "Amazon"
    Netflix = "Netflix"
    Google = "Google"
    Tesla = "Tesla"
    RiotBlockchain = "Riot AND Blockchain"
    VirginGalacticHoldings = "Virgin AND Galactic AND Holdings"
    
    # Search and save tweets for each query
    queries = [Facebook, Apple, Amazon, Netflix, Google, Tesla, RiotBlockchain, VirginGalacticHoldings]
    for query in queries:
        tweet_dataset = scraper.search_tweets(query)
        tweet_dataset.to_csv(f'{query}_tweet_dataset.csv', mode='a', index=False, header=False)
        print(f'{query} tweets saved successfully.')