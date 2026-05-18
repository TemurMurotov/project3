from service import get_matches
from db import save_json, load_json
from utils import print_news


matches = get_matches()

save_json(matches)

data = load_json()

print_news(data)
