# Generated by Django 3.1.2 on 2020-10-31 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20201031_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='coord',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='department',
            name='region',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='maps.region'),
        ),
        migrations.AlterField(
            model_name='region',
            name='coord',
            field=models.CharField(max_length=10000),
        ),
    ]
