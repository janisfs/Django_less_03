from django.shortcuts import render, redirect, get_object_or_404
from .models import News_post
from .forms import News_postForm
from django.views.generic import DetailView
from .models import News_post


# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'news_app/news.html', {'news': news})


def add_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была заполнена неверно'
    form = News_postForm()
    return render(request, 'news_app/add_news.html' , {'form': form, 'errors': error})


def news_detail(request, news_id):
    news_item = get_object_or_404(News_post, id=news_id)
    return render(request, 'news_app/news_detail.html', {'news': news_item})