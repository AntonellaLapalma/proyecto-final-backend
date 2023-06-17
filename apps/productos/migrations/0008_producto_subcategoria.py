# Generated by Django 4.1.7 on 2023-06-11 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_remove_producto_subcategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.subcategoria', verbose_name='sub categoría'),
        ),
    ]