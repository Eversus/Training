from django.forms import ModelForm, CharField
from .models import Post


class NewsForm(ModelForm):
    title = CharField(label='Название')
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'categories',
        ]

        labels = {
            'author': 'Автор',
            'categories': 'Категория'
        }