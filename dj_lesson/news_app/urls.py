from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='news_home'), # главная страница новостей
    path('add_news/', views.add_news, name='add_news'), # страница добавления новостей
    path('news/<int:news_id>/', views.news_detail, name='news_detail'), # страница детальной информации о новости
]
