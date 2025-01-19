from Book_author.models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['user','name', 'email', 'active']
        depth = 1
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'release_date', 'pages', 'active']
        depth = 1
        
        