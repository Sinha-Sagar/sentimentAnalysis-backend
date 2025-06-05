from textblob import TextBlob

def analyze_sentiment(comments):
    sentiment_result = {"positive": [], "neutral": [], "negative": []}

    for comment in comments:
        polarity = TextBlob(comment).sentiment.polarity
        if polarity > 0.1:
            sentiment_result["positive"].append(comment)
        elif polarity < -0.1:
            sentiment_result["negative"].append(comment)
        else:
            sentiment_result["neutral"].append(comment)

    total = len(comments)
    sentiment_percent = [
        {"label": "Positive", "value": round(len(sentiment_result["positive"]) * 100 / total, 2) if total else 0.0},
        {"label": "Neutral", "value": round(len(sentiment_result["neutral"]) * 100 / total, 2) if total else 0.0},
        {"label": "Negative", "value": round(len(sentiment_result["negative"]) * 100 / total, 2) if total else 0.0}
    ]

    return sentiment_result, sentiment_percent