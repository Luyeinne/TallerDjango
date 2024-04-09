from django.shortcuts import render, get_object_or_404
from .models import AutorDb, FraseDb, LibroDb
# from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    '''Esta es la pagina principal'''

    autor_list = AutorDb.objects.all().order_by("id")

    # autor_list es un Queryset
    return render(request, "index.html", {"autores": autor_list})

def AutorView(request, autor_id):
    autor = get_object_or_404(AutorDb, id=autor_id)
    lista_libros = LibroDb.objects.filter(autor_fk=autor)

    # autor = AutorDb.objects.filter(id=autor_id).first()
    # autor = AutorDb.objects.get(id=autor_id)

    # autor es un Objeto
    return render(
        request,
        "autor.html",
        {
            "autor": autor,
            "lista_libros": lista_libros,
        }
    )
