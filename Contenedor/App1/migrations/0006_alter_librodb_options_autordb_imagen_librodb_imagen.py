# Generated by Django 5.0.2 on 2024-03-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0005_remove_frasedb_autor_fk"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="librodb",
            options={"verbose_name": "Libro", "verbose_name_plural": "Libros"},
        ),
        migrations.AddField(
            model_name="autordb",
            name="imagen",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="imagenes_autor/",
                verbose_name="Imagen Autor",
            ),
        ),
        migrations.AddField(
            model_name="librodb",
            name="imagen",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="imagenes_libro/",
                verbose_name="Imagen Autor",
            ),
        ),
    ]
