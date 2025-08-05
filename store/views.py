from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Category

def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/book_list.html', {'books': books})

def author_books(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = author.books.all()
    return render(request, 'store/author_books.html', {'author': author, 'books': books})

def category_books(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    books = category.books.all()
    return render(request, 'store/category_books.html', {'category': category, 'books': books})
