# google-news-miner-summarizer


### Mines Google news links with user criteria:
 - google_news.period = '7d'  # News from last 7 days
 - google_news.max_results = 10  # number of responses across a keyword
 - google_news.country = 'United States'  # News from a specific country 
 - google_news.language = 'english'  # News in a specific language
 - google_news.exclude_websites = ['yahoo.com', 'cnn.com']  # Exclude news from specific website i.e Yahoo.com and CNN.com
 - google_news.start_date = (2020, 1, 1) # Search from 1st Jan 2020
 - google_news.end_date = (2020, 3, 1) # Search until 1st March 2020


Runs each link through newspaper.Article():
 - download
 - NLP summarize 
 - Print 
   - Keywords
   - title 
   - summary
 - Saves to newsMined.txt
  
Exception handling if news article retrieval fails:
  - prints "ERROR <link>"
  - saves error newsMined.txt

## How to run:
 - Git Clone 
 - pip install -r requirements.txt
 - python main.py

Prints "Task Done" on end
