# Generated by Django 4.0.5 on 2022-08-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artesanias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20, verbose_name='Nombre completo')),
                ('descripcion', models.TextField(max_length=100, verbose_name='Descripción general')),
                ('foto', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía')),
                ('municipio', models.TextField(max_length=50, verbose_name='Municipio de origen')),
                ('costo', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
