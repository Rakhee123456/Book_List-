from django.urls import path
from .views import AuthorList, AuthorDetail, BookList, BookDetail, AuthorDelete, AuthorUpdate 
from .auth_views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('authors/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
    path('authors/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    # path('books/create/', BookCreate.as_view(), name='book-create'),
    # path('books/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
    # path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    
    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
