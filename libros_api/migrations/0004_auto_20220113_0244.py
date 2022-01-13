# Generated by Django 3.2.11 on 2022-01-13 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_api', '0003_rename_género_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fechaPublicacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='segundoApellido',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
