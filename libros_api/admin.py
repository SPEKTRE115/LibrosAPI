from django.contrib import admin
from .models import Libro, Autor, Editorial, Genero

######################################################
# Registro de modelos de la aplicación               #
######################################################

#Regsitro de modelos
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Genero)