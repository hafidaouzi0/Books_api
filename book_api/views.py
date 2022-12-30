from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from book_api.models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def list_books(request):
     if request.method == 'GET':
       books= Book.objects.all()#complex data
      #books_python=list(books.values())#convert data to a list#python data structure
       #we need to convert this python DS to json
       serializer=BookSerializer(books,many=True)
       return Response(serializer.data)
    
@api_view(['POST'])
def book_create(request):
 if request.method == 'POST':
           serializer=BookSerializer(data=request.data)
           if serializer.is_valid():
            serializer.save()
            return Response(request.data)
 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





 #i should create  a view for get book by id

@api_view(['GET'])
def get_book(request,pk):
    try:
     book=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer=BookSerializer(book)
    return Response(serializer.data)


 #i should create  a view for updating a book

@api_view(['PUT'])
def update_book(request,pk):
      try:
       book=Book.objects.get(pk=pk)
      except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

      serializer=BookSerializer(book,data=request.data)
      if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   


 #i should create  a view for deleting a book

@api_view(['DELETE'])
def delete_book(request,pk):
     try:
      book=Book.objects.get(pk=pk)
     except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     book.delete()
     return Response({"delete":True},status=status.HTTP_204_NO_CONTENT)

