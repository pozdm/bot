import requests
import os
import json

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

url = os.getenv('URL') + "statistics/"

uris = {
    "Users statistics":        "users_stats",
    "UTM statistics":          "utm_stats",
    "Views statistics":        "views_stats",
    "Subscribers statistics":  "subscribers_stats",
    "Chats statistics":        "chats_stats",
    # "All statistics":         ["users_stats",
    #                            "utm_stats",
    #                            "views_stats",
    #                            "subscribers_stats",
    #                            "chats_stats"]
}


def get_stats_from_api(cat: str, start_date: str, end_date: str):

    params = {
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.get(url + uris[cat], params=params)
    result = response.json()

    return json.dumps(result, indent=4, ensure_ascii=False)


# print(get_stats_from_api("Views statistics", "2024-07-24", "2024-07-25"))
