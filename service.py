import requests


class News:
    def __init__(self, title, tournament):
        self.title = title
        self.tournament = tournament


def get_matches():
    url = "https://api.sofascore.com/api/v1/sport/football/events/live"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    matches = []

    events = data["events"]

    for event in events[:5]:

        home = event["homeTeam"]["name"]
        away = event["awayTeam"]["name"]

        title = f"{home} vs {away}"

        tournament = event["tournament"]["name"]

        match = News(title, tournament)

        matches.append({
            "title": match.title,
            "tournament": match.tournament
        })

    return matches