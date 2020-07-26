"""
app/summarizer.py
"""

import nltk
from newspaper import Article


def generate_summary(url: str) -> str:
    """
    generate a summary from an article
    """
    article = Article(url)
    article.download()
    article.parse()

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    return article.summary
