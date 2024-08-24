from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title': 'Home',
        'content': 'Главная страница няшности - UwU',
        'list': ['1st', '2nd'],
        'dict': {'1st': 1},
        'is_authenticated': False,

    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About Page')