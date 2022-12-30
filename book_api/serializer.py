from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields=["id",'title','number_of_pages','publish_date','quantity']
        #wwe can also do fields='__all__' 

         
