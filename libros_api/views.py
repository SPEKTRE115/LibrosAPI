from asyncio.windows_events import NULL
from http.client import HTTPResponse
from django.views import View
from .models import Libro
from .models import Autor
from .models import Genero
from .models import Editorial
from .serializers import LibroSerializer
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

######################################################
# Vistas de la API                                   #
######################################################



#Vista de la lista de todos los libros
class LibroListView(View):


    #MÉTODO GET
    def get(self,request):
        #Valida si se aplica un filtro por titulo o se buscan todos los resultados
        if('titulo' in request.GET):
            listaLibros = Libro.objects.filter(titulo__contains=request.GET['titulo'])
        else:
            listaLibros = Libro.objects.all()

        listaLibrosSerial = LibroSerializer(listaLibros, many=True).data

        return JsonResponse(list(listaLibrosSerial), safe=False)

    #MÉTODO POST
    def post(self,request, *args, **kwargs):
        jasonData = json.loads(request.body)

        #autoresData = Autor.objects.get(pk=jasonData['autores']) 
        #generosData=Genero.objects.get(pk=jasonData['generos'])

        libroNuevo = Libro.objects.create(
        titulo=jasonData['titulo'],
        numeroPaginas=jasonData['numeroPaginas'],
        fechaPublicacion=jasonData['fechaPublicacion'],
        editorial=Editorial.objects.get(pk =jasonData['editorial']),
        )
        
        #libroNuevo.autores.add(autoresData)
        #libroNuevo.generos.add(generosData)
        listaGeneros=jasonData['generos']
        
        for genero in listaGeneros:
            libroNuevo.generos.add(genero)

        libroNuevo.save()

        listaAutores=jasonData['autores']

        for autor in listaAutores:
            libroNuevo.autores.add(autor)
        
        libroNuevo.save()

        datos={'message':"Libro creado correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



#Vista de libros con pk específica
class LibroDetailView(View):
    #MÉTODO GET PK
    def get(self,request, pk):
        libro =  Libro.objects.filter(pk=pk)
        listaLibrosSerial = LibroSerializer(libro, many=True).data
        return JsonResponse(list(listaLibrosSerial), safe=False)

    #MÉTODO PUT
    def put(self,request, pk):
        jasonData = json.loads(request.body)
        libro = Libro.objects.get(pk=pk)
        libro.titulo=jasonData['titulo']
        #libro.autor=jasonData['autores']
        libro.numeroPaginas=jasonData['numeroPaginas']
        libro.fechaPublicacion=jasonData['fechaPublicacion']
        libro.editorial=Editorial.objects.get(pk =jasonData['editorial'])
        #libro.generos=jasonData['generos']

        listaGeneros=jasonData['generos']
        
        for genero in listaGeneros:
            libro.generos.add(genero)

        libro.save()

        listaAutores=jasonData['autores']

        for autor in listaAutores:
            libro.autores.add(autor)
        
        libro.save()

        datos={'message':"Libro actualizado correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DELETE
    def delete(self,request, pk):
        Libro.objects.filter(pk=pk).delete()
        datos={'message':"Libro borrado correctamente!"}
        return JsonResponse(datos)
    
    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



#Vista de la lista de todos los autores
class AutorListView(View):
    #MÉTODO GET
    def get(self,request):
        #Valida si se aplica un filtro por nombre o apellidos se buscan todos los resultados
        if('nombre' in request.GET):
            listaAutores = Autor.objects.filter(nombre__contains=request.GET['nombre'])
        elif('apellido' in request.GET):
            listaAutores = Autor.objects.filter(apellido__contains=request.GET['apellido'])
        elif('segundoApellido' in request.GET):
            listaAutores = Autor.objects.filter(segundoApellido__contains=request.GET['segundoApellido'])
        else:
            listaAutores = Autor.objects.all()

        return JsonResponse(list(listaAutores.values()), safe=False)

    #MÉTODO POST
    def post(self,request):
        jasonData = json.loads(request.body)
        Autor.objects.create(
        nombre=jasonData['nombre'],
        apellido=jasonData['apellido'],
        segundoApellido=jasonData['segundoApellido'],
        fechaNacimiento=jasonData['fechaNacimiento'],
        )
        datos={'message':"Autor creado correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#Vista de autores con pk específica
class AutorDetailView(View):
    #MÉTODO GET PK
    def get(self,request, pk):
        listaAutores = Autor.objects.get(pk=pk)
        return JsonResponse(model_to_dict(listaAutores))

    #MÉTODO PUT
    def put(self,request, pk):
        jasonData = json.loads(request.body)
        autor = Autor.objects.get(pk=pk)
        autor.nombre=jasonData['nombre']
        autor.apellido=jasonData['apellido']
        autor.segundoApellido=jasonData['segundoApellido']
        autor.fechaNacimiento=jasonData['fechaNacimiento']
        datos={'message':"Autor actualizado correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DELETE
    def delete(self,request, pk):
        Autor.objects.filter(pk=pk).delete()
        datos={'message':"Autor borrado correctamente!"}
        return JsonResponse(datos)
    
    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



#Vista de la lista de todos los géneros
class GeneroListView(View):
    #MÉTODO GET
    def get(self,request):
        #Valida si se aplica un filtro por nombre o se buscan todos los resultados
        if('nombre' in request.GET):
            listaGeneros = Genero.objects.filter(nombre__contains=request.GET['nombre'])
        else:
            listaGeneros = Genero.objects.all()

        return JsonResponse(list(listaGeneros.values()), safe=False)

    #MÉTODO POST
    def post(self,request):
        jasonData = json.loads(request.body)
        Genero.objects.create(nombre=jasonData['nombre'])
        datos={'message':"Género creado correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#Vista de generos con pk específica
class GeneroDetailView(View):
    #MÉTODO GET PK
    def get(self,request, pk):
        listaGeneros = Genero.objects.get(pk=pk)
        return JsonResponse(model_to_dict(listaGeneros))

    #MÉTODO PUT
    def put(self,request, pk):
        jasonData = json.loads(request.body)
        genero = Genero.objects.get(pk=pk)
        genero.nombre=jasonData['nombre'],
        datos={'message':"Género actualizado correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DELETE
    def delete(self,request, pk):
        Genero.objects.filter(pk=pk).delete()
        datos={'message':"Género borrado correctamente!"}
        return JsonResponse(datos)
    
    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#Vista de la lista de todas las editoriales
class EditorialListView(View):
    #MÉTODO GET
    def get(self,request):
        #Valida si se aplica un filtro por nombre o se buscan todos los resultados
        if('nombre' in request.GET):
            listaEditoriales = Editorial.objects.filter(nombre__contains=request.GET['nombre'])
        else:
            listaEditoriales = Editorial.objects.all()

        return JsonResponse(list(listaEditoriales.values()), safe=False)

    #MÉTODO POST
    def post(self,request):
        jasonData = json.loads(request.body)
        Editorial.objects.create(nombre=jasonData['nombre'])
        datos={'message':"Editorial creada correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#Vista de editorial con pk específica
class EditorialDetailView(View):
    #MÉTODO GET PK
    def get(self,request, pk):
        listaEditoriales = Editorial.objects.get(pk=pk)
        return JsonResponse(model_to_dict(listaEditoriales))

    #MÉTODO PUT
    def put(self,request, pk):
        jasonData = json.loads(request.body)
        editorial = Editorial.objects.get(pk=pk)
        editorial.nombre=jasonData['nombre'],
        datos={'message':"Editorial actualizada correctamente!"}
        return JsonResponse(datos)

    #MÉTODO DELETE
    def delete(self,request, pk):
        Editorial.objects.filter(pk=pk).delete()
        datos={'message':"Editorial borrada correctamente!"}
        return JsonResponse(datos)
    
    #MÉTODO DISPATCH, que se ejecuta con cada petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

