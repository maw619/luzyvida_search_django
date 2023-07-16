from django.db import models

 
class Libro(models.Model): 
    link1 = models.CharField(max_length=150, blank=True, null=True)
    link2 = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'libro'
    
    def __str__(self) -> str:
        return f"{self.name}"

class Capitulo(models.Model): 
    numero = models.IntegerField(blank=True, null=True)
    libro = models.ForeignKey('Libro', models.DO_NOTHING, null=True)

    class Meta:
        managed = True
        db_table = 'capitulo'
    
    def __str__(self) -> str:
        return f"{self.numero}"

class Versiculo(models.Model): 
    contenido = models.TextField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    capitulo = models.ForeignKey(Capitulo, models.DO_NOTHING, blank=True, null=True)
    #libro = models.ForeignKey(Libro, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'versiculo'

    def __str__(self) -> str:
        return f"{self.contenido}"

class Diccionario(models.Model): 
    palabra = models.CharField(max_length=100, blank=True, null=True)
    definicion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'diccionario'
 

class Tema(models.Model): 
    titulo = models.TextField(blank=True, null=True)
    verso_start = models.IntegerField(blank=True, null=True)
    verso_end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tema'

