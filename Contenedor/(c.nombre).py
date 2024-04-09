# coding: utf-8
a=AutorDb.objects.all()
a
a [0]
a [1]
a [2]
a [3]
a [4]
a [5]
b = a[0]
b
b.__dict__
b.frasedb_set.all()
for frase in b.frasedb_set.all():
    print(frase.cita)
    
a
c = a[5]
c
c.nombre=("Hare")
c.save
nombre.save
c
get_ipython().run_line_magic('save', '(c)')
