# Generated by Django 3.1.2 on 2020-10-31 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_auto_20201031_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='maps.region'),
        ),
    ]