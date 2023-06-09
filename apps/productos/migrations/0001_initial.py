# Generated by Django 4.1.7 on 2023-05-26 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombre', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='subcategoría')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('titulo_publicacion', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('imagen_publicacion', models.ImageField(default='default.jpg', upload_to='img/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria', verbose_name='categoría')),
                ('sub_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.subcategoria', verbose_name='sub categoría')),
            ],
        ),
    ]
