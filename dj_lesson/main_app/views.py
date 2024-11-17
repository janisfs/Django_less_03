from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')


# Создаем функцию для новой страницы
def new_page(request):
    return render(request, 'main_app/new_page.html')