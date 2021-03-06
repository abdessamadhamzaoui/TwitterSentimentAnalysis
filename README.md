# TwitterSentimentAnalysis
Sentiment Analysis for Ethereum and Eth related tweets

## Why?
Sentiment analysis is one of the most overlooked market indicators, even though it can give a clear idea of how the market thinks at a certain moment. Sentiment indicators look at how bullish or bearish market actors and what they are thinking and feeling, which can be used by investors and traders to predict the future behavior of the market.
What better place to see the opinions of eth holders than Twitter, famous for always having strong opinions.

## Software Architecture
![SoftwareArchitecture](https://raw.githubusercontent.com/abdessamadhamzaoui/TwitterSentimentAnalysis/main/architecture.jpg)
### Application Flow:
A python script running on a Compute Engine Instance fetches tweets that contain keywords or hashtags (in our case ETH and Ethereum) from Twitter using the Tweepy API wrapper. Tweets are fetched in the form of a stream, so this could be a problem since the stream might be more than the NLP API can handle. To solve this we use a PUB/SUB topic, the vm instance is the publisher and it publishes tweets as it gets them, then another script gets the tweets from the PUB/SUB topic (subscriber) one at a time. After this, the script sends tweets to the NLP ML API (which presents many advantages including supporting multiple languages).
The API gives each tweet a score between -1 and 1 based on how positive/negative the sentiment is, and a magnitude between 0 and +inf based on how strong the emotion is.
After we have the scores, we can send them to BigQuery to do further analysis, otherwise we just sum the total scores (score x magnitude).
## Results:
Results for Saturday 28th March 2021 after analyzing over 3400 tweets containing the hashtags #Ethereum and #ETH :
![Result](https://raw.githubusercontent.com/abdessamadhamzaoui/TwitterSentimentAnalysis/main/result-saturday.jpg)
