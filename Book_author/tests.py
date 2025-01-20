from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Book

# Create your tests here.

# testcase for author model
class BookAuthorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(user=self.user, name='Test Author', email='author@example.com')
        self.book = Book.objects.create(title='Test Book', author=self.author, release_date='2025-01-01', pages=100)

    def test_author_creation(self):
        self.assertEqual(self.author.name, 'Test Author')
        self.assertEqual(self.author.email, 'author@example.com')

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, self.author)

    def test_author_string_representation(self):
        self.assertEqual(str(self.author), 'Test Author')

    def test_book_string_representation(self):
        self.assertEqual(str(self.book), 'Test Book')

    def test_author_book_relationship(self):
        self.assertIn(self.book, self.author.book_set.all())

    def test_author(self):
        self.assertEqual(1, 1)

# class AutheticationTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.author = Author.objects.create(user=self.user, name='Test Author', email='author@example.com')
#         self.book = Book.objects.create(title='Test Book', author=self.author, release_date='2025-01-01', pages=100)

#     def test_author_book_relationship(self):
#         self.assertIn(self.book, self.author.book_set.all())
class LoginTestCase(TestCase):
    def setUp(self):
    
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(user=self.user, name='Test Author', email='author@example.com')
        self.book = Book.objects.create(title='Test Book', author=self.author, release_date='2025-01-01', pages=100)
        data={
            'username': 'testuser',
            'password': 'testpass'
        }

    def test_author_book_relationship(self):
        self.assertIn(self.book, self.author.book_set.all())

    