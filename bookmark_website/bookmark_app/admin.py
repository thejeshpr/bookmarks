from django.contrib import admin

from .models import Category, Bookmark


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'timestamp', 'updated_at')
    list_filter = ('timestamp', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'updated_at'


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'desc',
        'title',
        'slug',
        'url',
        'timestamp',
        'updated_at',
    )
    list_filter = ('category', 'timestamp', 'updated_at')
    search_fields = ('slug',)
    date_hierarchy = 'updated_at'