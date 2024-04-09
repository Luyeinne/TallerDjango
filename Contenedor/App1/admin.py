from django.contrib import admin
from .models import AutorDb, FraseDb, LibroDb
from django.core.exceptions import ValidationError
from django.forms import ModelForm

# Register your models here.

admin.site.site_header = "Hola Luyeinne Soler"
admin.site.index_title = "Hola Libros"
admin.site.site_title = "Luyeinne"

class LibroInLine(admin.TabularInline):
    model = LibroDb
    extra = 1

class FraseInLine(admin.TabularInline):
    model = FraseDb
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_nacimiento", "fecha_fallecimiento", "profesion", "nacionalidad", "imagen"]
    list_display = ["nombre"]

    inlines = [LibroInLine]


    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1 = obj.nombre
                obj.nombre = nombre1.replace("O", "o")
                obj.save()

        self.message_user(request,"Exitosamente")

    actualizar_o.short_description = "Actualizar letras O"

    actions = ["actualizar_o"]

admin.site.register(AutorDb, AutorAdmin)


@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "Libro_fk"]
    list_display = ["cita"]


@admin.register(LibroDb)
class LibroAdmin(admin.ModelAdmin):
    fields = ["nombre", "editorial", "fecha_publicacion", "autor_fk", "imagen"]
    list_display = ["nombre"]
    inlines = [FraseInLine]
