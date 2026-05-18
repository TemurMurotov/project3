from service import get_news
from db import save_json, load_json
from utils import print_news


news = get_news()

save_json(news)

data = load_json()

print_news(data)