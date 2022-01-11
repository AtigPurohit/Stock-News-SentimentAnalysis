from NewsExtraction import Extraction
from SentimentAnalysis import SentimentScore

if __name__ == "__main__":
    company_name = input("Enter the company name -  ")

    df = Extraction(company_name)
    print(df)

    score = SentimentScore(df)
    print(score)


