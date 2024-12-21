from django.contrib import admin
from .models import Book, Genre, Author

# Registering the Genre model
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registering the Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registering the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'year', 'language', 'genre')
    list_filter = ('author', 'year', 'genre')
    search_fields = ('name', 'author__name', 'genre__name')
