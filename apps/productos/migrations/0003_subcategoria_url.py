# Generated by Django 4.1.7 on 2023-05-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_categoria_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
