# Generated by Django 4.1.7 on 2023-04-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_blog_model_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_model',
            name='likes',
        ),
        migrations.AddField(
            model_name='blog_model',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
