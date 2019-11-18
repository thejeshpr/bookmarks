from django import forms
from django.forms import ModelForm
from django.utils import timezone

from .models import Bookmark, Category


class CategoryForm(ModelForm):    
    class Meta:
        model = Category
        fields = [
            'name'
        ]


class BookmarkForm(ModelForm):    
    class Meta:
        model = Bookmark
        fields = [
            'url',
            'title',
            'category',
            'desc',
            'tags'
        ]

    