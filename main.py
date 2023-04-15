from newspaper import Article
from gnews import GNews


news_for = "Scotia Bank"

google_news = GNews(news_for)


google_news.period = "7d"  # News from last 7 days
google_news.max_results = 10  # number of responses across a keyword
# google_news.country = "United States"  # News from a specific country
google_news.language = "english"  # News in a specific language
# google_news.exclude_websites = []
# google_news.start_date = (2020, 1, 1)  # Search from 1st Jan 2020
# google_news.end_date = (2020, 3, 1)  # Search until 1st March 2020

# result = google_news.get_news('"Citadel-securities"')


json_resp = google_news.get_news("Scotia Bank")

with open("newsMined.txt", "w") as f:
    for i in range(10):
        link = json_resp[i]["url"]
        try:
            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            print(
                f"\nArticle Title: \t{article.title}\nArticle Keywords: \t{article.keywords}\nArticle Summary: \n{article.summary}\n\n\n"
            )
            f.write(
                f"\nArticle Title: \t{article.title}\nArticle Keywords: \t{article.keywords}\nArticle Summary: \n{article.summary}\n\n\n"
            )
        except:
            print(f"ERROR!!!! for link: {link}\n")
            f.write(f"ERROR!!!! for link: {link}\n")


print("Task Done")
