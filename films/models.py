from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # the Film model has a foreign key column called genre, with a one-to-many relationship
    
    def __str__(self):
        return self.title