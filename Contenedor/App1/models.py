from django.db import models

# Create your models here.
class AutorDb(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento", null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha Fallecimiento", null=True, blank=True)
    profesion = models.CharField(verbose_name="Profesion", max_length=50, null=False, blank=False)
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50 )
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen Autor", null=True, blank=True)

    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return self.nombre


class LibroDb(models.Model):
    nombre = models.CharField(verbose_name="Nombre Libro", max_length=50)
    editorial = models.CharField(verbose_name="Editorial", max_length=50)
    fecha_publicacion = models.DateField(verbose_name="Fecha publicacion")
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen libro", null=True, blank=True)


    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self) -> str:
        return self.nombre

class FraseDb(models.Model):
    cita = models.TextField(verbose_name="Cita", max_length=400)
    Libro_fk = models.ForeignKey(LibroDb, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    def __str__(self) -> str:
        return self.cita

