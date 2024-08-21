from ai_assistant import ai_assistant
from newspaper import Article


def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()

    return ai_assistant("summarize this article", article.text)


def create_headline(url):
    article = Article(url)
    article.download()
    article.parse()

    headline_response = ai_assistant(
        "create a catchy headline for this article", article.text
    )
    headline = headline_response.split('" "')

    return headline


msg = create_headline(
    "https://edition.cnn.com/2024/08/19/travel/switzerland-munitions-removal-scli-intl/index.html"
)
print(msg)
