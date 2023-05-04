from NewsExtraction import Extraction
from SentimentAnalysis import SentimentScore

if __name__ == "__main__":
    company_name = input("Enter the company name or any topic you want news on -  ")

    df = Extraction(company_name)
    print(df)
  #sdgdsfh
    score = SentimentScore(df)
    print(score)


