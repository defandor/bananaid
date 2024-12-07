import hashlib
import os
import uuid
import ipinfo

from loguru import logger


from bananaid.settings import DEBUG, ALLOWED_COUNTRIES


def gen_url_query(redirect_to=None):
    url = f'?u={hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()}&secret={hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()}'
    if redirect_to:
        url += f'&success_url={redirect_to}'
    return url


def get_request_ip(request):
    if DEBUG or 'dinamo' in request.path:
        return os.getenv('IP')

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


ipinfo_handler = ipinfo.getHandler(os.getenv('IPINFO_ACCESS_TOKEN'))


def ip2country_access(ip_address):
    try:
        logger.info(f'start looking up ip [{ip_address}]')
        ip_details = ipinfo_handler.getDetails(ip_address)
        for country in ALLOWED_COUNTRIES.split(','):
            if ip_details.country in country:
                logger.success(f'{ip_address} - {country} is allowed')
                return {'allowed': True, 'country': f'{ip_details.country_flag["emoji"]} # {ip_details.country_name} # {ip_details.country_flag["emoji"]}', 'city': ip_details.city, 'region': ip_details.region, 'postal': ip_details.postal, }

        logger.warning(f'NEW IP {ip_address}->{ip_details.country_name}  not allowed using ipinfo ')
        return {'allowed': False, 'country': ip_details.country_name, 'city': ip_details.city, 'region': ip_details.region}
    except Exception as ex:
        logger.error(ex)
        return {'Raised': True, 'allowed': True}
