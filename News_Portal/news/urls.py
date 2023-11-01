from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewsDetail

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view()),
   # pk — это первичный ключ новости, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', NewsDetail.as_view()),
]