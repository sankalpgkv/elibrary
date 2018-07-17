from django.views import generic
from .models import Book, Review
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, ReviewForm
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'libapp/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()

class DetailView(generic.DetailView):
    model = Book 
    template_name = 'libapp/details.html'

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'libapp/login.html', context) 

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('libapp:index')
            else:
                return render(request, 'libapp/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'libapp/login.html', {'error_message': 'Invalid login'})
    return render(request, 'libapp/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('libapp:index')
    context = {
        "form": form,
    }
    return render(request, 'libapp/registration_form.html', context)

def rate(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
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

def review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    try:
        review = Review()
        review.book = Book.objects.get(pk=book_id)
        review.review_text = request.POST['review']
        review.user = request.user.username
        review.save()
    except(KeyError):
        return render(request, 'libapp/details.html', { 
        'book': book,
        'error_message': "Cannot submit an empty review",    
        })
    else:
        all_reviews = book.review_set.all()
        book.save()
        context = {
            'all_reviews' : all_reviews,
            'book' : book
        }
        return render(request , 'libapp/details.html', context)        
