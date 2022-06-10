from django.contrib import admin

from .models import Book, Genre, ImageBook, PersonReader, Author


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(ImageBook)
admin.site.register(Author)
admin.site.register(PersonReader)
