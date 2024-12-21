from django.db import models
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='books')
    year = models.IntegerField(null=True)
    language = models.TextField(null=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
