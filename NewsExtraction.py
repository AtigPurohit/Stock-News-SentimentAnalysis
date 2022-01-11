from GoogleNews import GoogleNews
import pandas as pd
import datetime as dt
from newspaper import Article
from newspaper import Config

def Extraction(name):

    today = dt.date.today()
    today = today.strftime('%m-%d-%Y')
    yesterday = dt.date.today() - dt.timedelta(days=1)
    yesterday = yesterday.strftime('%m-%d-%Y')

    # We need config because sometimes the newspaper package shows errors in downloading the articles
    # We use the agent variable to get authorized
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
    config = Config()
    config.browser_agent = agent
    config.request_timeout = 10

    if name != "":
        googlenews = GoogleNews(start=yesterday, end=today)
        googlenews.search(name)  # searching for the news available on the company name
        results = googlenews.results()  # storing the fetched articles in results

        df = pd.DataFrame(results)  # creating the dataset
        # print(df.head())
        # print(df.info())
    else:
        print("Please enter a valid company name")

    try:
        list = []  # creating an empty list
        for i in df.index:
            dict = {}
            article = Article(df['link'][i], config=config)
            try:
                article.download()  # downloading the article
                article.parse()  # parsing the article
                article.nlp()  # performing natural language processing (nlp)
            except:
                pass
            # storing the data in our dictionary
            dict['Date'] = df['date'][i]
            dict['Title'] = article.title
            dict['Article'] = article.text
            dict['Summary'] = article.summary

            list.append(dict)
        check_empty = not any(list)
        # print(check_empty)
        if check_empty == False:
            news_df = pd.DataFrame(list)  # creating dataframe
            return news_df

    except Exception as e:
        # exception handling

        print("exception occurred:" + str(e))
        return 'Some error occured, please try again with a different name'