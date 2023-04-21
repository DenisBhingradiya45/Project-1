# Generated by Django 4.2 on 2023-04-21 09:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0032_remove_blog_model_likes_blog_model_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_model',
            name='likes',
        ),
        migrations.AddField(
            model_name='blog_model',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
