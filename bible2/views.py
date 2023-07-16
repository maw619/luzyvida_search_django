from django.shortcuts import render, redirect
from biblia.models import Libro, Versiculo, Capitulo
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.db.models.functions import StrIndex



def search_bible(request):
    libro = Libro.objects.all()
    if request.method == 'GET':
        q = request.GET.get('query')
        
        if q:   
            vector = SearchVector('contenido')
            query=SearchQuery(q) 
            search_headline = SearchHeadline('contenido', query)
            results = Versiculo.objects.filter(contenido__search=query)
            #results = Versiculo.objects.annotate(search=vector).filter(search=query)
            #results = Versiculo.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.01).order_by('-rank')
            #results = Versiculo.objects.annotate(rank=SearchRank(vector, query)).annotate(headline=search_headline).filter(rank__gte=0.01, contenido__icontains=q).order_by('-rank')

            # Calculate multiplied rank
            # for result in results:
            #     result.multiplied_rank = 100 / result.rank  
 
            return render(request, 'bible2/search_results.html', {'results': results,'count':results.count(),'libro':libro})
        else:
            results = []
        return render(request, 'bible2/search_results.html',{'libro':libro})
 


def my_view(request, capitulo_numero, libro_name):  
    libro = Libro.objects.all()
    versiculos = Versiculo.objects.filter(capitulo__numero=capitulo_numero, capitulo__libro__name=libro_name).order_by('numero')
    cap = Capitulo.objects.filter(libro__name=libro_name)
    libros = Libro.objects.filter(name=libro_name).values_list('id', flat=True)
    index = libros.get()
    print(f"Index: {index}")

    get_libro = Libro.objects.get(id=index)

    name = ""
    chapter = ""
    for x in versiculos:
        name = x.capitulo.libro.name
        chapter = x.capitulo.numero

    chapter_count = cap.count() 

    next_capitulo_numero = int(capitulo_numero) + 1
    prev_capitulo_numero = int(capitulo_numero) - 1 
    print("chapter count: ", chapter_count)
    print("current chapter count: ", capitulo_numero) 

    if int(capitulo_numero) > chapter_count:
        next_capitulo_numero = 1
        capitulo_numero = 1  # Reset capitulo_numero to 1
        print("current chapter count new: ", capitulo_numero)
        print("reached its limit") 
        index = index + 1 
 
    temp_libro_name = "" 

    if int(capitulo_numero) < 2:
        print("low limit")
        temp_index = index - 1
        temp_libro_name = Libro.objects.get(id=temp_index)
        print("prev book: ", temp_libro_name)

    
    if next_capitulo_numero > chapter_count:
        temp_index = index + 1
        temp_libro_name = Libro.objects.get(id=temp_index)
        print(temp_libro_name)
    if prev_capitulo_numero < 1:
        print("low limit prev_capitulo_numero")
        temp_index = index - 1
        temp_libro_name = Libro.objects.get(id=temp_index)
        print(temp_libro_name)
 

    temp_next_capitulo_numero = 1
    context = {
        'versiculos': versiculos,
        'name': get_libro.name,
        'chapter': chapter,
        'capitulo_numero': capitulo_numero,
        'next_capitulo_numero': next_capitulo_numero,
        'prev_capitulo_numero': prev_capitulo_numero,
        'chapter_count': chapter_count,
        'libro_name': libro_name,
        'temp_libro_name': temp_libro_name,
        'temp_next_capitulo_numero':temp_next_capitulo_numero,
        'libro':libro

    }

    return render(request, 'bible2/chapter.html', context)


def book_by_chapter(request):
    pass
