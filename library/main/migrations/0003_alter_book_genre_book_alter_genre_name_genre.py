# Generated by Django 4.0.5 on 2022-06-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_author_first_name_alter_author_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre_book',
            field=models.ManyToManyField(to='main.genre', verbose_name='Жанры книг'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name_genre',
            field=models.CharField(max_length=30, unique=True, verbose_name=''),
        ),
    ]
