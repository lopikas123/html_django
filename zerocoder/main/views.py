from django.shortcuts import render
from django.http import HttpResponse

def data(request):
    return HttpResponse("<h1>Первая страница с контентом</h1>")

def test(request):
    return HttpResponse("<h1>Вторая страница с контентом</h1>")