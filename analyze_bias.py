import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def main():
    df = pd.read_csv("results/raw_responses.csv")
    analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(text):
        score = analyzer.polarity_scores(text)["compound"]
        if score > 0.2:
            return "positive"
        elif score < -0.2:
            return "negative"
        else:
            return "neutral"

    df['sentiment'] = df['response'].apply(get_sentiment)
    sentiment_summary = df.groupby(['model', 'prompt_name', 'sentiment']).size().unstack(fill_value=0)
    os.makedirs("analysis", exist_ok=True)
    sentiment_summary.to_csv("analysis/sentiment_summary.csv")
    print("Sentiment analysis done.")

if __name__ == "__main__":
    main()

#filepath modified for security