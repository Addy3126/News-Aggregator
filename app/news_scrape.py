# Description: This program scrapes and summarizes news articles from the New York Times.

from newspaper import Article


# Summarizes the article and provides valuable information regarding the article metadata, including images and
# attributions.
def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()
    # Punkt is a sentence tokenizer that is useful for extracting and detecting text.
    article.download('punkt')
    article.nlp()

    # Gets the author or authors of the article
    author_string = " "
    for author in article.authors:
        author_string += author  # adds all authors (if more than 1) to the author string.

    # Gets the publication date of the article
    date = article.publish_date

    # strftime() converts a tuple or struct_time representing a time to a string as specified by the format argument.
    # Here, it is used to mark the month, day, and year of the date in a readable format.
    publish_date = " " + str(date.strftime("%m/%d/%Y"))

    # Gets the top image of the article
    img_url = "Top Image Url: " + str(article.top_image)

    # Gets the article images
    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image  # adds a newline and a tab before each image is printed

    return {"author_string": author_string, "publish_date": publish_date, "img_url": img_url,
            "image_string": image_string, "article_summary": article.summary}

