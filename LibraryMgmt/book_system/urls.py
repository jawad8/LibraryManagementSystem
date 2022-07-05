from django.urls import path
from . import views

urlpatterns = [
    path('fetchBooks/', views.fetchAllBooks),
    path('addBooks/', views.addBook),
    path('updateBooks/', views.updateBook),
    path('deleteBooks/', views.deleteBook),
]
