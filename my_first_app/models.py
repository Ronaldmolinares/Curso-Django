from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.TextField(max_length=100)
    year = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f"{self.name} modelo {self.year}"

class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name} con dirección {self.address}"

class Author(models.Model):
    name = models.TextField(max_length=100)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name} nacido el {self.birth_date}"
    
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f"Perfil de {self.author.name}"
    
class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField(null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='authors', blank=True)

    def __str__(self):
        return f"{self.title} de {self.publication_date} publicado por {self.publisher.name}"

