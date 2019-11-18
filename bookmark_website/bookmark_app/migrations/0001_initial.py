# Generated by Django 2.2.7 on 2019-11-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category Name', max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, help_text='Description', null=True)),
                ('title', models.CharField(blank=True, help_text='bookmark title', max_length=500, null=True, unique=True)),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('url', models.URLField(blank=True, help_text='URL', max_length=2000, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(help_text='Category', on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='bookmark_app.Category')),
            ],
        ),
    ]
