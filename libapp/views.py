from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    all_books = Book.objects.all() 
    context = { 'all_books' : all_books, }
    return render(request, 'libapp/index.html' , context) 

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'libapp/details.html', { 'book': book })

def rate(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book=get_object_or_404(Book, pk=book_id)
    rate_value = '0'
    try:
        rate_value = request.POST['rate_val'] 
    except (KeyError):
        return render(request, 'libapp/details.html', { 
        'book': book,
        'error_message': "You did not select a valid choice.",    
        })
    else:    
        book.rating=book.rating*book.num_votes+int(rate_value)
        if int(rate_value)!=0:
            book.num_votes+=1
        book.rating/=book.num_votes
        book.save()
        return render(request , 'libapp/details.html', { 'book' : book })