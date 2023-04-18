from newspaper import Article
from gnews import GNews
import streamlit as st

news_for = ""
num = 0


news_for = st.text_input(label="Search news for ?")

num = int(st.slider(label="Input no. of Articles", min_value=1, max_value=10))


button = st.button(label="Mine NEWS")


def main():
    google_news = GNews(news_for)

    google_news.period = "7d"  # News from last 7 days
    google_news.max_results = num  # number of responses across a keyword
    # google_news.country = "United States"  # News from a specific country
    google_news.language = "english"  # News in a specific language
    # google_news.exclude_websites = []
    # google_news.start_date = (2020, 1, 1)  # Search from 1st Jan 2020
    # google_news.end_date = (2020, 3, 1)  # Search until 1st March 2020

    json_resp = google_news.get_news(news_for)

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

        except:
            st.text_area(
                label=f"Error Fetching Article {i+1}",
                value=f"LINK: {link}",
            )

    st.caption(body="# TASK DONE")


if button:
    main()
