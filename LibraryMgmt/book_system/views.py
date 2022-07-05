from statistics import mode
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from book_system import models
from book_system import serializers
# Create your views here.

@api_view(['GET'])
# API for fetching all the books
def fetchAllBooks(request):
    try:
        print("1")
        books_query = models.BOOKS.objects.all()
        books_obj = serializers.BooksSerializer(books_query, many=True)
        print(books_obj.data)
        return Response(books_obj.data,status=200)    
    except Exception as e:
        print("2")
        return Response(False,status=400)

@api_view(['POST'])
# API for adding a book
def addBook(request):
    try:
        reqData = request.data
        print(reqData)
        print("reqData")

        return Response(True,status=201)
    except Exception as e:
        return Response(False,status=400)

@api_view(['POST'])
#  API for updating book
def updateBook(request):
    try:
        reqData = request.data
        return Response(True,status=201)
    except Exception as e:
        return Response(False,status=400)

@api_view(['POST'])
#  API for deleting a book
def deleteBook(request):
    try:
        reqData = request.data
        
    except Exception as e:
        return Response(False,status=400)
