all_stats = """
<strong>Ежедневная статистика по аудитории ЯЗЖ за {{ date }}:</strong>  
<strong>Всего пользователей(с декабря 2022): {{ total_users }} ({{ "{:+}".format(total_users_delta or 0) }})</strong>

<strong>Пользователей: {{ unique_users }} ({{ "{:+}".format(unique_users_delta or 0) }})</strong>  
<strong>Просмотров: {{ views }} ({{ "{:+}".format(views_delta or 0) }})</strong>

<strong>UTM term:</strong>
{% for key, value in utm_stats.result_for_end_day.items() -%}
{{ loop.index0 + 1 }}. {{ key }}: {{ value }} ({{ "{:+}".format(utm_stats.delta[key] or 0) }})
{% endfor %}
<strong>Просмотры по сервисам:</strong>
{% for key, value in views_stats.result_for_end_day.items() -%}
{{ loop.index0 + 1 }}. {{ key }}: {{ value }} ({{ "{:+}".format(views_stats.delta[key] or 0) }})
{% endfor %}
<strong>Подписки на уведомления: </strong>  
Telegram: {{ subscribers_tg }} ({{ "{:+}".format(subscribers_tg_delta or 0) }})  
VK: {{ subscribers_vk }} ({{ "{:+}".format(subscribers_vk_delta or 0) }})  
Всего (уникальных): {{ subscribers_total }} ({{ "{:+}".format(subscribers_total_delta or 0) }})

<strong>Домовые чаты (пилот):</strong>  
Всего чатов: {{ chats }} ({{ "{:+}".format(chats_delta or 0) }})  
Всего участников: {{ chats_users }} ({{ "{:+}".format(chats_users_delta or 0) }})  
Всего сообщений: {{ chats_messages }} ({{ "{:+}".format(chats_messages_delta or 0) }})
"""

users_stats = """
<strong>Всего пользователей(с декабря 2022): {{ total_users }} ({{ "{:+}".format(total_users_delta or 0) }})</strong>

<strong>Пользователей: {{ unique_users }} ({{ "{:+}".format(unique_users_delta or 0) }})</strong>  
<strong>Просмотров: {{ views }} ({{ "{:+}".format(views_delta or 0) }})</strong>"""

utm_stats = """
<strong>UTM term:</strong>
{% for key, value in utm_stats.result_for_end_day.items() -%}
{{ loop.index0 + 1 }}. {{ key }}: {{ value }} ({{ "{:+}".format(utm_stats.delta[key] or 0) }})
{% endfor %}"""

views_stats = """
<strong>Просмотры по сервисам:</strong>
{% for key, value in views_stats.result_for_end_day.items() -%}
{{ loop.index0 + 1 }}. {{ key }}: {{ value }} ({{ "{:+}".format(views_stats.delta[key] or 0) }})
{% endfor %}"""

subscribers_stats = """<strong>Подписки на уведомления: </strong>  
Telegram: {{ subscribers_tg }} ({{ "{:+}".format(subscribers_tg_delta or 0) }})  
VK: {{ subscribers_vk }} ({{ "{:+}".format(subscribers_vk_delta or 0) }})  
Всего (уникальных): {{ subscribers_total }} ({{ "{:+}".format(subscribers_total_delta or 0) }})"""

chats_stats = """<strong>Домовые чаты (пилот):</strong>  
Всего чатов: {{ chats }} ({{ "{:+}".format(chats_delta or 0) }})  
Всего участников: {{ chats_users }} ({{ "{:+}".format(chats_users_delta or 0) }})  
Всего сообщений: {{ chats_messages }} ({{ "{:+}".format(chats_messages_delta or 0) }})"""