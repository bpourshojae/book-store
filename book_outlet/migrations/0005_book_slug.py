# Generated by Django 5.1.4 on 2025-01-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_book_author_book_is_bestselling_alter_book_ratting'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
