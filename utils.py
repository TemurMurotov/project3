def print_news(data):

    for item in data:
        print("Match:", item["title"])
        print("Tournament:", item["tournament"])
        print("-" * 30)