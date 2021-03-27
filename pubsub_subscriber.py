from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import json
from google.cloud import language_v1

client = language_v1.LanguageServiceClient()
f = open("tosend.txt", "a")

project_id = ""
subscription_id = ""
# Number of seconds the subscriber should listen for messages
timeout = 60.0
client = language_v1.LanguageServiceClient()
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path('','')

def callback(message):
    data = json.loads(message.data)
    texts= data['text']
    print(f"Received {texts}")
    document = language_v1.Document(content=texts, type_=language_v1.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    scorefinal = sentiment.score*sentiment.magnitude
    f.write(str(scorefinal)+'\n')
    message.ack()


streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()
