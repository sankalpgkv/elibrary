from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    all_books = Book.objects.all() 
    context = { 'all_books' : all_books, }
    return render(request, 'libapp/index.html' , context) 

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'libapp/details.html', { 'book': book })