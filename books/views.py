from django.shortcuts import render
# Tenemos que importar los modelos que vayamos a usar
from .models import Author, Genre
# Create your views here.


def home(request):

    # obtener los autores
    authors = Author.objects.all()
    print(authors)

    for author in authors:
        print(author.name, author.nationality)

    authors1 = Author.objects.get(id=1)
    print(authors1.id)

    # Si la vista esta dentro de una carpeta llamada templates la pon go directamente
    return render(request, './home.html')


def insert(request):
    new_genre = Genre.objects.create(genre='Horror')
    print(new_genre)

    # Si la vista esta dentro de una carpeta llamada templates la pon go directamente
    return render(request, './insert.html')


def update(request):

    update_genre = Genre.objects.get(id=1)

    print(update_genre)
    if (update_genre.genre == 'Fantasy'):
        update_genre.genre = 'Horror'
        update_genre.save()
        return render(request, './update.html')
    update_genre.genre = "Fantasy"
    update_genre.save()

    return render(request, './update.html')


def delete(request):

    delete_genre = Genre.objects.get(id=1)
    delete_genre.delete()

    return render(request, "./delete.html")
