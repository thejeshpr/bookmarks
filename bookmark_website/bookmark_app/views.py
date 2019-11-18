from django.db.models import Sum, Count
# from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.views import generic
from django.views.generic import edit
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Bookmark, Category
from .forms import BookmarkForm, CategoryForm
# import zap.helper as helper


class Home(generic.ListView):
    model = Bookmark
    context_object_name = 'bookmarks'
    template_name = 'bookmark_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['additional_info'] = helper.get_home_page_data()
        return context


class CategoryCreateView(edit.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'bookmark_app/category-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['page'] = 'car-add'
        # context['title'] = 'Add new car'
        # context['heading'] = 'Add new car'
        return context


class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'bookmark_app/categories-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['additional_info'] = helper.get_home_page_data()
        return context

# =========================================
class BookmarkCreateView(edit.CreateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name = 'bookmark_app/bookmark-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['page'] = 'car-add'
        # context['title'] = 'Add new car'
        # context['heading'] = 'Add new car'
        return context