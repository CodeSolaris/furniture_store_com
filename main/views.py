from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "About - о нас",
        "content": "О нас",
        "text_on_page": "текст о том почему магазин такой классный и почему такой нужный товар.",
    }
    return render(request, "main/about.html", context=context)
