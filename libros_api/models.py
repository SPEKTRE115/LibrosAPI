from django.db import models


######################################################
# Modelos de la API                                  #
######################################################

#Modelo de los objetos de tipo Autor
class Autor(models.Model):
    #Atributos de un Autor
    nombre = models.CharField(max_length=255, verbose_name = "Nombre")
    apellido = models.CharField(max_length=255, verbose_name = "Apellido")
    segundoApellido = models.CharField(max_length=255,blank=True, verbose_name = "Segundo apellido")
    fechaNacimiento = models.DateField(editable=True,verbose_name = "Fecha nacimiento",blank=True,null=True)

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.segundoApellido

    class Meta:
         verbose_name = "Autor"
         verbose_name_plural = "Autores"

#Modelo de los objetos de tipo Editorial
class Editorial(models.Model):
    #Atributos de un Editorial
    nombre = models.CharField(max_length=255,verbose_name = "Nombre")

    def __str__(self):
        return self.nombre

    class Meta:
         verbose_name = "Editorial"
         verbose_name_plural = "Editoriales"

#Modelo de los objetos de tipo Género
class Genero(models.Model):
    #Atributos de un Género
    nombre = models.CharField(max_length=255,verbose_name = "Nombre")

    def __str__(self):
        return self.nombre

    class Meta:
         verbose_name = "Género"
         verbose_name_plural = "Géneros"

#Modelo de los objetos de tipo Libro
class Libro(models.Model):
    #Atributos de un Libro
    titulo = models.CharField(max_length=255,verbose_name = "Título")
    autores = models.ManyToManyField(Autor,verbose_name = "Autores",blank=True)
    numeroPaginas = models.IntegerField(default=0,verbose_name = "Número de páginas")
    fechaPublicacion = models.DateField(editable=True,verbose_name = "Fecha publicación",blank=True,null=True)
    editorial = models.ForeignKey('Editorial',models.CASCADE,verbose_name = "Editorial")
    generos = models.ManyToManyField(Genero, verbose_name="Géneros",blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
         verbose_name = "Libro"
         verbose_name_plural = "Libros"
