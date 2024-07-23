from django.contrib import admin

# importar los modelos
from .models import Nationality, Author, Genre, Book


class AuthorAdmin(admin.ModelAdmin):
    # list_display = ('name', 'date of birth', ' country') Esto estaria mal, tienen que coincidir
    list_display = ('name', 'dob', 'nationality')


class BookAdmin    (admin.ModelAdmin):
    list_display = ('title', 'author', 'year_published')


# Register your models here.
admin.site.register(Nationality)
admin.site.register(Author, AuthorAdmin)  # Tengo que registrar todo
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
