# Generated by Django 5.0.6 on 2024-06-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
