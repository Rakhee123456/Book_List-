from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.http import Http404
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
class AuthorList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        # Check if the user is the owner of the author profile
        if hasattr(author, 'user') and author.user != request.user and not request.user.is_staff:
            return Response({'error': 'You do not have permission to edit this author'}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_object(pk)
        # Check if the user is the owner of the author profile or staff
        if hasattr(author, 'user') and author.user != request.user and not request.user.is_staff:
            return Response({'error': 'You do not have permission to delete this author'}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        # Check if the user is the author's owner or staff
        if (hasattr(book.author, 'user') and 
            book.author.user != request.user and 
            not request.user.is_staff):
            return Response({'error': 'You do not have permission to edit this book'}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        # Check if the user is the author's owner or staff
        if (hasattr(book.author, 'user') and 
            book.author.user != request.user and 
            not request.user.is_staff):
            return Response({'error': 'You do not have permission to delete this book'}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)