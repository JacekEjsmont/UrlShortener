from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import ShortUrl

import random


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def process_url(request):
    original_url = request.GET.get('url')
    try:
        url_in_database = ShortUrl.objects.get(original_url=original_url)
        data = {'shorten_url': url_in_database.shorted_url}

    except:
        short = random.randint(0, 100000000)
        short = str(short)
        ShortUrl.objects.create(short=short, shorted_url='https://urlje.herokuapp.com/urlshort/' + short, original_url=original_url)
        data = {'shorten_url': 'https://urlje.herokuapp.com/urlshort/' + short}
    return JsonResponse(data)


def open_shorten_url(request, short):
    short_url = ShortUrl.objects.get(short=short)
    return redirect(short_url.original_url)
