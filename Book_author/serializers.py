from Book_author.models import Author, Book
from rest_framework import serializers
from django.utils import timezone


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'username', 'name', 'email', 'active', 'books_count', 'first_name', 'last_name']
        read_only_fields = ['id']
        depth = 1

    def get_books_count(self, obj):
        return obj.book_set.count()

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required")
        return value.lower()


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    email = serializers.CharField(source='author.email', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'release_date', 'pages', 'active', 'email']
        read_only_fields = ['id']
        depth = 1

    def validate_pages(self, value):
        if value <= 0:
            raise serializers.ValidationError("Pages must be greater than 0")
        return value

    def validate_release_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Release date cannot be in the future")
        return value