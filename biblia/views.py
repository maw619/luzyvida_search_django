from django.shortcuts import render, redirect
from .models import Capitulo, Libro, Diccionario, Tema, Versiculo
from django.http import JsonResponse
from unidecode import unidecode


def home(request):
    libro = Libro.objects.all()
    book_id = request.GET.get('id')
    for x in Libro.objects.all():
        print(x.name)
    if request.method == 'POST':
        book_id = request.POST.get('id')
        chapters = Capitulo.objects.filter(libro_id=book_id).all()
        
        print("Count on Chapters: ", chapters)
        # for x in chapters:
        #     print(f"{x.numero} :::: {x.libro}")
        #     v = Versiculo.objects.filter(capitulo_id=x.id)
        #     for y in v:    
        #         print(f"{y.contenido}")
        context = {'libro': libro, 'chapters': chapters}
    else:
        context = {'libro': libro}

    return render(request, 'biblia/home.html', context)

def get_chapters(request):
    book_id = request.GET.get('book_id')
    chapters = Capitulo.objects.filter(libro_id=book_id).values('id', 'numero')
    return JsonResponse(list(chapters), safe=False)

def get_verses(request):
    chapter_id = request.GET.get('chapter_id')
    verses = Versiculo.objects.filter(capitulo_id=chapter_id).values('id', 'numero', 'contenido')
    return JsonResponse(list(verses), safe=False)