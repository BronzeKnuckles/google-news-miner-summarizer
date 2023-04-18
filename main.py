from newspaper import Article
from gnews import GNews
import streamlit as st

news_for = ""
num = 0

# news_for = "Scotia Bank"
news_for = st.text_input(label="Search news for ?")
# num = st.number_input(label="Input no. of articles")
num = st.slider(label="Input no. of Articles", min_value=1, max_value=10)


def main():
    google_news = GNews(news_for)

    google_news.period = "7d"  # News from last 7 days
    google_news.max_results = 10  # number of responses across a keyword
    # google_news.country = "United States"  # News from a specific country
    google_news.language = "english"  # News in a specific language
    # google_news.exclude_websites = []
    # google_news.start_date = (2020, 1, 1)  # Search from 1st Jan 2020
    # google_news.end_date = (2020, 3, 1)  # Search until 1st March 2020

    # result = google_news.get_news('"Citadel-securities"')

    json_resp = google_news.get_news(news_for)

    # with open("newsMined.txt", "w") as f:
    for i in range(int(num)):
        link = json_resp[i]["url"]
        try:
            article = Article(link)
            article.download()
            article.parse()
            article.nlp()
            st.text_area(
                label=f"Article no. {i+1}",
                height=350,
                value=f"Article Title: \t{article.title}\n\nArticle Keywords: \t{article.keywords}\n\nArticle Summary: \n{article.summary}",
            )
            print(
                f"\n{i+1}. Article Title: \t{article.title}\nArticle Keywords: \t{article.keywords}\nArticle Summary: \n{article.summary}\n\n\n"
            )
            # f.write(f"\n{i+1}. Article Title: \t{article.title}\nArticle Keywords: \t{article.keywords}\nArticle Summary: \n{article.summary}\n\n\n")
        except:
            print(f"ERROR!!!! for link no. {i+1}: {link}\n")
            st.text_area(
                label=f"Error Fetching Article {i+1}",
                height=350,
                value=f"LINK: {link}",
            )

            # f.write(f"ERROR!!!! for link no. {i+1}: {link}\n")

    print("Task Done")


if news_for != "" and num != 0:
    main()
    news_for = ""
    num = 0
