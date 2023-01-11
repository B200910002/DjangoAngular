from django.db import models

# Create your models here.

class Book(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookTitle = models.CharField(max_length=100)
    BookCategorie = models.CharField(max_length=100)
    BookAuthor = models.CharField(max_length=100)
    BookPrice = models.CharField(max_length=100)
    Date = models.DateField()

class Categories(models.Model):
    CategorieId = models.AutoField(primary_key=True)
    CategorieType = models.CharField(max_length=100)

