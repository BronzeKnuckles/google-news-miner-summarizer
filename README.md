# google-news-miner-summarizer

---
Forked from [ranahaani/GNews](https://github.com/ranahaani/GNews)

### Mines Google news links with user criteria then prints and stores the news title, keywords and summary.
```
google_news.period = '7d'  # News from last 7 days
google_news.max_results = 10  # number of responses across a keyword
 - edit num_of_results
google_news.country = 'United States'  # News from a specific country 
google_news.language = 'english'  # News in a specific language
google_news.exclude_websites = ['yahoo.com', 'cnn.com']  # Exclude news from #specific website i.e Yahoo.com and CNN.com
google_news.start_date = (2020, 1, 1) # Search from 1st Jan 2020
google_news.end_date = (2020, 3, 1) # Search until 1st March 2020
```
---
**Runs each link through newspaper.Article():**
 1. Download article
 2. NLP summarize 
 3. Print:
    - Keywords
    - Title 
    - Summary
 4. Saves to newsMined.txt
 5. Print: "Task Done" when complete

---
*Exception handling if news article retrieval fails:*
  - prints "ERROR with link"
  - saves the same to newsMined.txt
---
## **How to run:**
 - Git Clone 
 - pip install -r requirements.txt
 - python main.py (Note : company name, number of results and other parameters are in main.py)


## Output in [newsMined.txt](https://github.com/BronzeKnuckles/google-news-miner-summarizer/blob/master/newsMined.txt)




#### Ignore streamlitapp.py -> made streamlit app


