from django.urls import path
from django.contrib import admin
from book_api.views import list_books,book_create,get_book,update_book,delete_book

urlpatterns=[

path("list/",list_books),
path('',book_create),
path('<int:pk>/',get_book),
path('update/<int:pk>',update_book),
path('delete/<int:pk>',delete_book)

]