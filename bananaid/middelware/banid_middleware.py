from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django_user_agents.utils import get_user_agent
from loguru import logger

from bananaid.const import PageRedirection
from bananaid.telegrambot import new_visit
from bananaid.utils import get_request_ip, ip2country_access


class BanIDMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        try:
            if request.session.get('banned'):
                return HttpResponseRedirect('/' + PageRedirection.NOT_ALLOWED_PAGE.value)
            if not request.session.get('ip'):
                allowed = True
                user_agent = get_user_agent(request)
                request.session['ip'] = get_request_ip(request)
                request.session['device'] = str(user_agent)
                if user_agent.is_bot or 'other' in str(user_agent).lower():
                    logger.warning(f'Bot Not allowed to access {str(user_agent)} for ip[{request.session.get("ip")}]')
                    allowed = False

                ip_access = ip2country_access(request.session['ip'])
                for key, value in ip_access.items():
                    request.session[key] = value

                if ip_access['allowed'] is False:
                    allowed = False

                if allowed:
                    logger.success(f'Access granted for {request.session.get("ip")} and user agent {str(user_agent)}]')
                    new_visit(user_agent, ip_access, request.session['ip'])
                    return self.get_response(request)

                else:
                    request.session['allowed'] = False
                    request.session['banned'] = True
                    return HttpResponseRedirect('/' + PageRedirection.NOT_ALLOWED_PAGE.value)

            else:
                if request.session.get('allowed'):
                    logger.success(f'ip {request.session.get("ip")}[{request.session.get("device")}] already allowed')
                    return self.get_response(request)
                else:
                    return HttpResponseRedirect('/' + PageRedirection.NOT_ALLOWED_PAGE.value)

        except Exception as e:
            logger.error(f'access middleware skipped withe Exception while processing request {e}')
            return self.get_response(request)