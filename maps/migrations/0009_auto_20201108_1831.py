# Generated by Django 3.1.2 on 2020-11-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_favorite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['user'], 'verbose_name': 'Favori', 'verbose_name_plural': 'Favoris'},
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='name',
        ),
        migrations.AddField(
            model_name='favorite',
            name='article',
            field=models.CharField(default='null', max_length=10000, verbose_name='Article'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='title',
            field=models.CharField(default='null', max_length=1000, verbose_name='Titre'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='url',
            field=models.CharField(default='null', max_length=1000, verbose_name='Lien'),
        ),
    ]
