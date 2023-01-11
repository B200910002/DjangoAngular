from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BookApp.models import Categories,Book
from BookApp.serializers import CategoriesSerializer,BookSerializer



# Create your views here.
@csrf_exempt
def CategorieApi(request,id=0):
    if request.method=='GET':
        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)

    elif request.method=='POST':
        categorie_data=JSONParser().parse(request)
        categorie_serializer=CategoriesSerializer(data=categorie_data)
        if categorie_serializer.is_valid():
            categorie_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        categorie_data=JSONParser().parse(request)
        categorie=Categories.objects.get(CategorieId=categorie_data['CategorieId'])
        categorie_serializer=CategoriesSerializer(categorie, data=categorie_data)
        if categorie_serializer.is_valid():
            categorie_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        categorie=Categories.objects.get(CategorieId=id)
        categorie.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

    else:
        return JsonResponse("all thingks failed!!", safe=False)


@csrf_exempt
def BookApi(request,id=0):
    if request.method=='GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)

    elif request.method=='POST':
        book_data=JSONParser().parse(request)
        book_serializer=BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        book_data=JSONParser().parse(request)
        book=Book.objects.get(BookId=book_data['BookId'])
        book_serializer=BookSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        book=Book.objects.get(BookId=id)
        book.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

    else:
        return JsonResponse("all thingks failed!!", safe=False)
