from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'главная страница магазина - Home Page',
        'list': ['first', 'second'],
        'dict': {'key': 'value'},
        'is_authenticated': True,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page")