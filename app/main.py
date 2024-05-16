# Imports all the methods and variables from each script.
from news_extract import *
from news_scrape import *
from news_nlp import *
import time
from newspaper.article import ArticleException

from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Gets all the latest URL's from the NY Times Technology Section. (see news_extract.py for more detail)
    content_string = get_content_string(my_url)
    starts, ends = find_occurrences(content_string)
    url_list = get_all_urls(starts, ends, content_string)
    contents = []

    # Gets the article summary and performs sentiment analysis on the chosen URL.
    # For more information on how this works, visit news_scrape.py and news_nlp.py!
    for url in url_list:
        try:
            article_url = str(url)
            article_stuff = summarize_article(url)
            sentiment = find_sentiment(article_stuff['article_summary'])
            content = {
                "article_url": article_url,
                "sentiment": sentiment
            }
            content.update(article_stuff)
            contents.append(content)
        except ArticleException:
            pass
    return render_template('index.html', contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
