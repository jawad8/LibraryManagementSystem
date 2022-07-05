from django.shortcuts import render
from points_system import serializers
from points_system import models
from accounts import models as accountModels
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
# API for fetching all the books
def fetchAllBooks(request):
    try:
        books_query = models.Books.objects.all()
        books_obj = serializers.getBookSerializer(books_query, many=True)
        return Response(books_obj.data,status=200)    
    except Exception as e:
        return Response(False,status=400)

@api_view(['POST'])
# API for adding a book
def addBook(request):
    try:
        reqData = request.data
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
