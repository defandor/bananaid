import hashlib
import uuid
from ip2geotools.databases.noncommercial import DbIpCity

from bananaid.settings import DEBUG, DEFAULT_IP, ALLOWED_COUNTRIES


def gen_url_query():
    return f'?u={hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()}&secret={hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()}'


def get_request_ip(request):
    if DEBUG:
        return DEFAULT_IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def ip2country_access(ip_address):
    if DEBUG:
        return True
    try:
        loc = DbIpCity.get(ip_address, api_key='free')
        for country in ALLOWED_COUNTRIES.split(','):
            if loc.country in country:
                return True
        return False
    except Exception as ex:
        print(ex)
