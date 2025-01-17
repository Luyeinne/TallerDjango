# Generated by Django 5.0.2 on 2024-03-22 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0003_alter_frasedb_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="LibroDb",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=50, verbose_name="Nombre Libro"),
                ),
                (
                    "editorial",
                    models.CharField(max_length=50, verbose_name="Editorial"),
                ),
                (
                    "fecha_publicacion",
                    models.DateField(verbose_name="Fecha publicacion"),
                ),
                (
                    "autor_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App1.autordb"
                    ),
                ),
            ],
            options={
                "verbose_name": "Libros",
            },
        ),
        migrations.AddField(
            model_name="frasedb",
            name="Libro_fk",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="App1.librodb",
            ),
            preserve_default=False,
        ),
    ]
