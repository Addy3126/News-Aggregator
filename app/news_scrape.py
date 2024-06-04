from newspaper import Article


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()
    # Punkt is a sentence tokenizer that is useful for extracting and detecting text.
    article.download('punkt')
    article.nlp()

    article_title = article.title

    author_lst = []
    for author in article.authors:
        author_lst.append(author)
    author_string = ', '.join(author_lst)  # adds all authors (if more than 1) to the author string.

    date = article.publish_date

    publish_date = " " + str(date.strftime("%m/%d/%Y"))

    img_url = "Top Image Url: " + str(article.top_image)

    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image  # adds a newline and a tab before each image is printed

    return {"article_title": article_title, "author_string": author_string, "publish_date": publish_date,
            "img_url": img_url, "image_string": image_string, "article_summary": article.summary}

