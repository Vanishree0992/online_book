from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('author/<int:author_id>/', views.author_books, name='author_books'),
    path('category/<int:category_id>/', views.category_books, name='category_books'),
]
