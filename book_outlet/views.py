from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Max, Min

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-title")
    book_numbers = books.count()
    avg_ratting = books.aggregate(Avg("ratting"))
    return render(request, 'book_outlet/index.html', {'books':books,'total_number_books':book_numbers,'average_ratting':avg_ratting})

def book_detail(request, slug):
    # try:    
    #     book = Book.objects.get(id=ide)
    # except:
    #     raise Http404()  
    book = get_object_or_404(Book, slug=slug)  
    return render(request, 'book_outlet/book_detail.html', {
        'title':book.title,
        'author':book.author,
        'ratting':book.ratting,
        'is_bestseller':book.is_bestselling
    })