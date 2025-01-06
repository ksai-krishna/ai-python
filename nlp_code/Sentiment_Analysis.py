#install textblob
from textblob import TextBlob

# Sample text for sentiment analysis
text = "I absolutely love this phone!"

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis and get the polarity
polarity = blob.sentiment.polarity

# Print sentiment result based on polarity
if polarity > 0:
    print("Positive Sentiment")
elif polarity < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")