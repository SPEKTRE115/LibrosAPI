# Generated by Django 4.0.1 on 2022-01-13 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_api', '0014_rename_autor_libro_autores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(blank=True, to='libros_api.Autor', verbose_name='Autores'),
        ),
    ]
