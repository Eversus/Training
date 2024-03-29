from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter
from .models import Post, Author
from django import forms

# Создаем свой набор фильтров для модели Post.
class NewsFilter(FilterSet):
    name = CharFilter(field_name='title',
                      label="Название",
                      lookup_expr='icontains')
    author = ModelChoiceFilter(field_name='author',
                               queryset= Author.objects.all(),
                               label="Автор", empty_label='Все')
    date = DateFilter(field_name='time_in',
                      widget=forms.DateInput(attrs={'type': 'date'}),
                      lookup_expr='gt',
                      label='Поиск по дате начиная с')
    class Meta:
        model = Post
        fields = [
            'name', 'author', 'date'
        ]