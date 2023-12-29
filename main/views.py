from django.shortcuts import render
from goods.models import Categories

# Create your views here.
def index(request):
    
    categories = Categories.objects.all()
    
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }
    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "About - о нас",
        "content": "О нас",
        "text_on_page": "текст о том почему магазин такой классный и почему такой нужный товар.",
    }
    return render(request, "main/about.html", context=context)
