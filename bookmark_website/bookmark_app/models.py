from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text='Category Name')
    slug = models.CharField(max_length=50, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:        
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        # return reverse('bookmark_app:home', kwargs={'cpk': self.car.pk, 'pk': self.pk})
        return reverse('bookmark_app:home')


class Bookmark(models.Model):    
    category = models.ForeignKey(
                        'Category', on_delete=models.CASCADE, 
                        related_name='bookmarks', help_text='Category')
    desc = models.TextField(blank=True, null=True, help_text='Description')
    title = models.CharField(max_length=500, unique=True, blank=True, null=True, help_text='bookmark title')
    slug = models.CharField(max_length=500, unique=True)
    url = models.URLField(max_length=2000, blank=True, null=True, help_text="URL")
    tags = TaggableManager()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def __repr__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Bookmark, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        # return reverse('bookmark_app:home', kwargs={'cpk': self.car.pk, 'pk': self.pk})
        return reverse('bookmark_app:home')
