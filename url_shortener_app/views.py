from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import ShortUrl

import random


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def process_url(request):
    original_url = request.GET.get('url')
    print(original_url)
    try:
        url_in_database = ShortUrl.objects.get(original_url=original_url)
        print('try')
        data = {'shorten_url': 'http://127.0.0.1:8000/urlshort/' + url_in_database.short}

    except:
        short = random.randint(0, 100000000)
        short = str(short)
        print('except')
        ShortUrl.objects.create(short=short, original_url=original_url)
        data = {'shorten_url': 'http://127.0.0.1:8000/urlshort/' + short}

    return JsonResponse(data)


def open_shorten_url(request, short):
    short_url = ShortUrl.objects.get(short=short)
    return redirect(short_url.original_url)
