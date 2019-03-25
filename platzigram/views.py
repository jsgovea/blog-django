from django.http import HttpResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    return HttpResponse('Oh, hi current server time is {now}'.format(now=now))


def hi(request):
    return HttpResponse('hi!')


def sort_integers(request):
    return HttpResponse('Sort Integers')
