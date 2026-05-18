def print_news(news):
    for item in news:
        print("Title:", item["title"])
        print("Link:", item["link"])
        print("-" * 40)