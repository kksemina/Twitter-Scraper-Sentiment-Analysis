import tweepy
from tweepy import OAuthHandler
import pandas as pd


print("Inputing Credentials;")

access_token = 'YOUR ACCESS KEY HERE'
access_token_secret = 'YOUR ACCESS KEY HERE'
consumer_key = 'YOUR ACCESS KEY HERE'
consumer_secret = 'YOUR ACCESS KEY HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit =True)

print("Starting to Scrape!")

"""Twitter will automatically sample the last 7 days of data. Depending on how many total tweets there are with the specific hashtag, keyword, handle, or key phrase that you are looking for, you can set the date back further by adding since= as one of the parameters. You can also manually add in the number of tweets you want to get back in the items() section."""

Facebook =  "Facebook"
Apple = "Apple"
Amazon = "Amazon"
Netflix = "Netflix"
Google = "Google"
Tesla = "Tesla"
RiotBlockchain = "Riot AND Blockchain"
VirginGalacticHoldings = "Virgin AND Galactic AND Holdings"


#--------------------------------------
#Facebook
facebook_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'urls'])

print("Facebook tweets")
for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= Facebook, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count,
        tweet.retweet_count, tweet.full_text.encode('utf-8'), tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'urls'])
        facebook_tweet_dataset = facebook_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
facebook_tweet_dataset.to_csv('Facebook_tweet_dataset.csv', mode='a', index=False, header=False)


#--------------------------------------
#Apple
print("Apple tweets")

apple_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text','urls'])


for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= Apple, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'),tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'urls'])
        apple_tweet_dataset= apple_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
apple_tweet_dataset.to_csv('Apple_tweet_dataset.csv', mode='a', index=False, header=False)


#--------------------------------------
#Amazom
print("Amazon tweets")

amazon_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'urls'])


for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= Amazon, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'),tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', "urls"])
        amazon_tweet_dataset= amazon_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
amazon_tweet_dataset.to_csv('Amazon_tweet_dataset.csv', mode='a', index=False, header=False)


#--------------------------------------
#Netflix

print("Netflix tweets")

netflix_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', "urls"])


for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= Netflix, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'),tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', "urls"])
        netflix_tweet_dataset= netflix_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
netflix_tweet_dataset.to_csv('Netflix_tweet_dataset.csv', mode='a', index=False, header=False)


#--------------------------------------
#Google
google_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'urls'])

print("Google tweets")
for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= Google, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'), tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'urls'])
        google_tweet_dataset = google_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
google_tweet_dataset.to_csv('Google_tweet_dataset.csv', mode='a', index=False, header=False)



#--------------------------------------
#Tesla
tesla_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', "urls"])

print("Tesla tweets")
for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= Tesla, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'),tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text','urls'])
        tesla_tweet_dataset = tesla_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
tesla_tweet_dataset.to_csv('Tesla_tweet_dataset.csv', mode='a', index=False, header=False)



#----------------------------------------------------


#RiotBlockchain 
RiotBlockchain_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text','urls'])

print("RiotBlockchain tweets")
for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= RiotBlockchain, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'),tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text','urls'])
        RiotBlockchain_tweet_dataset = RiotBlockchain_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
RiotBlockchain_tweet_dataset.to_csv('RiotBlockchain_tweet_dataset.csv', mode='a', index=False, header=False)



#_________________________________

VirginGalacticHoldings = "Virgin AND Galactic AND Holdings"
#VirginGalacticHoldings
VirginGalacticHoldings_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text','urls'])

print("VirginGalacticHoldings tweets")
for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= VirginGalacticHoldings, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'),tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', "urls"])
        VirginGalacticHoldings_tweet_dataset = VirginGalacticHoldings_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
VirginGalacticHoldings_tweet_dataset.to_csv('VirginGalacticHoldings_tweet_dataset.csv', mode='a', index=False, header=False)


#_________________________________
Microsoft = "Microsoft"

#Microsoft
Microsoft_tweet_dataset = pd.DataFrame(columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', "urls"])

print("Microsoft tweets")
for tweet in tweepy.Cursor(api.search_tweets, tweet_mode='extended', q= Microsoft, lang="en").items(500):
        appending_dataframe = pd.DataFrame([[tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8'), tweet.entities['urls']]], columns=['Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text', 'urls'])
        Microsoft_tweet_dataset = Microsoft_tweet_dataset.append(appending_dataframe)
        

#tweet_dataset.to_csv('tweet_dataset.csv', index=False)
Microsoft_tweet_dataset.to_csv('Microsoft_tweet_dataset.csv', mode='a', index=False, header=False)



print("Done!")
