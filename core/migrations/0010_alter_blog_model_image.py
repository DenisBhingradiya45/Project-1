# Generated by Django 4.1.7 on 2023-04-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_blog_model_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_model',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
