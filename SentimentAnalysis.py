import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

def percentage(part,whole):
    return 100 * float(part)/float(whole)



#Iterating over the tweets in the dataframe
def SentimentScore(news_df):

    # Assigning Initial Values
    positive = 0
    negative = 0
    neutral = 0
    # Creating empty lists
    news_list = []
    neutral_list = []
    negative_list = []
    positive_list = []

    for news in news_df['Summary']:
        news_list.append(news)
        analyzer = SentimentIntensityAnalyzer().polarity_scores(news)
        neg = analyzer['neg']
        neu = analyzer['neu']
        pos = analyzer['pos']
        comp = analyzer['compound']

        if neg > pos:
            negative_list.append(news)  # appending the news that satisfies this condition
            negative += 1  # increasing the count by 1
        elif pos > neg:
            positive_list.append(news)  # appending the news that satisfies this condition
            positive += 1  # increasing the count by 1
        elif pos == neg:
            neutral_list.append(news)  # appending the news that satisfies this condition
            neutral += 1  # increasing the count by 1

    positive = percentage(positive, len(news_df))  # percentage is the function defined above
    negative = percentage(negative, len(news_df))
    neutral = percentage(neutral, len(news_df))

    dict = {'Positive - ':positive, 'Negative - ':negative, 'Neutral - ':neutral}
    return dict