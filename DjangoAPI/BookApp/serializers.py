from rest_framework import serializers
from BookApp.models import Categories, Book

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = (  'CategorieId',
                    'CategorieType')
                    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (  'BookId',
                    'BookTitle',
                    'BookCategorie',
                    'BookAuthor',
                    'BookPrice',
                    'Date')