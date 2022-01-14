from django.urls import path
from .views import LibroListView, LibroDetailView
from .views import AutorListView, AutorDetailView
from .views import EditorialListView, EditorialDetailView
from .views import GeneroListView, GeneroDetailView,Principal

######################################################
# URLS de la API                                     #
######################################################


#URLS
urlpatterns = [
    path('', Principal.as_view(), name='home'),
    path('libro/', LibroListView.as_view(), name="lista de libros"),
    path('libro/<int:pk>', LibroDetailView.as_view(), name="libro"),
    path('autor/', AutorListView.as_view(), name="lista de autores"),
    path('autor/<int:pk>', AutorDetailView.as_view(), name="autor"),
    path('editorial/', EditorialListView.as_view(), name="lista de editoriales"),
    path('editorial/<int:pk>', EditorialDetailView.as_view(), name="editorial"),
    path('genero/', GeneroListView.as_view(), name="lista de generos"),
    path('genero/<int:pk>', GeneroDetailView.as_view(), name="genero"),
]