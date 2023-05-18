from newspaper import Article
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname("."))

from gnews import GNews


news_for = input("Input the news search word")
num_of_results = int(input("Input the number of search results"))


def main():
    google_news = GNews(news_for)

    google_news.period = "7d"  # News from last 7 days
    google_news.max_results = num_of_results  # number of responses across a keyword
    # google_news.country = "United States"  # News from a specific country
    google_news.language = "english"  # News in a specific language
    # google_news.exclude_websites = []
    # google_news.start_date = (2020, 1, 1)  # Search from 1st Jan 2020
    # google_news.end_date = (2020, 3, 1)  # Search until 1st March 2020

    json_resp = google_news.get_news(news_for)

    with open("newsMined.txt", "w") as f:
        for i in range(num_of_results):
            link = json_resp[i]["url"]
            try:
                article = Article(link)
                article.download()
                article.parse()
                article.nlp()

                print(
                    f"\n{i+1}. Article Title: \t{article.title}\nArticle Keywords: \t{article.keywords}\nArticle Summary: \n{article.summary}\n\n\n"
                )
                f.write(
                    f"\n{i+1}. Article Title: \t{article.title}\nArticle Keywords: \t{article.keywords}\nArticle Summary: \n{article.summary}\n\n\n"
                )
            except:
                print(f"ERROR!!!! for link no. {i+1}: {link}\n")
                f.write(f"ERROR!!!! for link no. {i+1}: {link}\n")

    print("Task Done")


if news_for != "":
    main()
