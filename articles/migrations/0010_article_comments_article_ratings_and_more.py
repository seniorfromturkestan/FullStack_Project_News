# Generated by Django 4.2 on 2023-05-14 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='articles_comments', to='articles.comment'),
        ),
        migrations.AddField(
            model_name='article',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='articles_ratings', to='articles.rating'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_connect_comment', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_connect_rating', to='articles.article'),
        ),
    ]
