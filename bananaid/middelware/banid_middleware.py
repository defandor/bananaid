from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from bananaid.utils import get_request_ip, ip2country_access


class BanIDMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        if not request.session.get('ip'):
            request.session['device'] = str(request.user_agent)
            request.session['ip'] = get_request_ip(request)
            request.session['allowed'] = ip2country_access(request.session.get('ip'))

        elif request.session.get('ip') and request.session.get('allowed'):
            return self.get_response(request)

        elif request.session.get('ip') and not request.session.get('allowed'):
            return HttpResponseRedirect('https://www.google.no/')

        if not request.session.get('allowed'):
            return HttpResponseRedirect('https://www.google.no/')

        return self.get_response(request)
