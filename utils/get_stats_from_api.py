import requests
import os
import json

import jinja2

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from templates import output_templates

url = os.getenv('URL') + "statistics/"

uris = {
    "Users statistics":        "users_stats",
    "UTM statistics":          "utm_stats",
    "Views statistics":        "views_stats",
    "Subscribers statistics":  "subscribers_stats",
    "Chats statistics":        "chats_stats",
    "All statistics":         ["users_stats",
                               "utm_stats",
                               "views_stats",
                               "subscribers_stats",
                               "chats_stats"]
}


def get_stats_from_api(cat: str, start_date: str, end_date: str):

    params = {
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.get(url + uris[cat], params=params)
    result = response.json()

    match cat:
        case "Users statistics":
            template = jinja2.Template(output_templates.users_stats)
            return template.render(
                total_users=result.get("result_for_end_day", {}).get("total_users"),
                total_users_delta=result.get("delta", {}).get("total_users"),
                unique_users=result.get("result_for_end_day", {}).get("users_for_day"),
                unique_users_delta=result.get("delta", {}).get("users_for_day"),
                views=result.get("result_for_end_day", {}).get("views_for_day"),
                views_delta=result.get("delta", {}).get("views_for_day"),
            )
        case "UTM statistics":
            template = jinja2.Template(output_templates.utm_stats)
            return template.render(
                utm_stats=result
            )
        case "Views statistics":
            template = jinja2.Template(output_templates.views_stats)
            return template.render(
                views_stats=result
            )
        case "Subscribers statistics":
            template = jinja2.Template(output_templates.subscribers_stats)
            return template.render(
                subscribers_tg=result.get("result_for_end_day", {}).get("tg"),
                subscribers_tg_delta=result.get("delta", {}).get("tg"),
                subscribers_vk=result.get("result_for_end_day", {}).get("vk"),
                subscribers_vk_delta=result.get("delta", {}).get("vk"),
                subscribers_total=result.get("result_for_end_day", {}).get("total"),
                subscribers_total_delta=result.get("delta", {}).get("total"),
            )
        case "Chats statistics":
            template = jinja2.Template(output_templates.chats_stats)
            return template.render(
                chats=result.get("result_for_end_day", {}).get("chats"),
                chats_delta=result.get("delta", {}).get("chats"),
                chats_users=result.get("result_for_end_day", {}).get("users"),
                chats_users_delta=result.get("delta", {}).get("users"),
                chats_messages=result.get("result_for_end_day", {}).get("messages"),
                chats_messages_delta=result.get("delta", {}).get("messages")
            )
        case "All result":
            template = jinja2.Template(output_templates.all_stats)
            return template.render(
                total_users=result.get("result_for_end_day", {}).get("total_users"),
                total_users_delta=result.get("delta", {}).get("total_users"),
                unique_users=result.get("result_for_end_day", {}).get("users_for_day"),
                unique_users_delta=result.get("delta", {}).get("users_for_day"),
                views=result.get("result_for_end_day", {}).get("views_for_day"),
                views_delta=result.get("delta", {}).get("views_for_day"),
                utm_stats=result,
                views_stats=result,
                subscribers_tg=result.get("result_for_end_day", {}).get("tg"),
                subscribers_tg_delta=result.get("delta", {}).get("tg"),
                subscribers_vk=result.get("result_for_end_day", {}).get("vk"),
                subscribers_vk_delta=result.get("delta", {}).get("vk"),
                subscribers_total=result.get("result_for_end_day", {}).get("total"),
                subscribers_total_delta=result.get("delta", {}).get("total"),
                chats=result.get("result_for_end_day", {}).get("chats"),
                chats_delta=result.get("delta", {}).get("chats"),
                chats_users=result.get("result_for_end_day", {}).get("users"),
                chats_users_delta=result.get("delta", {}).get("users"),
                chats_messages=result.get("result_for_end_day", {}).get("messages"),
                chats_messages_delta=result.get("delta", {}).get("messages")
            )

    return result


# print(get_stats_from_api("Views statistics", "2024-07-24", "2024-07-25"))
