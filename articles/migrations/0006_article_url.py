# Generated by Django 4.2 on 2023-05-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_genre_article_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
