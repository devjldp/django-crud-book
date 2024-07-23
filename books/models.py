from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Nationality(models.Model):
    country = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country


class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # Formato YYYY-MM-DD en bases de datos SQL. Lo mismo para el formulario.
    dob = models.DateField(verbose_name="Date of birth")
    # Prevent deletion if nationality is used
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150, unique=True)
    # Prevent deletion if genre is used
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    # Delete book if author is deleted
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year_published = models.IntegerField(validators=[MinValueValidator(
        -2000), MaxValueValidator(9999)])  # Ensure valid year
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(5)])  # Rating between 1 and 5

    def __str__(self):
        return self.title
