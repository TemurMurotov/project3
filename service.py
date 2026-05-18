import requests
from bs4 import BeautifulSoup


class News:
    def __init__(self, title, link):
        self.title = title
        self.link = link


def get_news():
    url = "https://kun.uz"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    news_list = []

    articles = soup.find_all("a", class_="small-news__title")

    for article in articles[:5]:
        title = article.text.strip()
        link = article.get("href")

        if link.startswith("/"):
            link = "https://kun.uz" + link

        news = News(title, link)

        news_list.append({
            "title": news.title,
            "link": news.link
        })

    return news_list