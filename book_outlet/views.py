from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {'books':books})

def book_detail(request, ide):
    # try:    
    #     book = Book.objects.get(id=ide)
    # except:
    #     raise Http404()  
    book = get_object_or_404(Book, id=ide)  
    return render(request, 'book_outlet/book_detail.html', {
        'title':book.title,
        'author':book.author,
        'ratting':book.ratting,
        'is_bestseller':book.is_bestselling
    })