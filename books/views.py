from django.shortcuts import render
from django.urls import reverse
from .models import Book

# Create your views here.

def chooseBook(request):
    books = Book.objects.all()
    return render(request, 'books/choose-book.html', {
        "books" : books
    })


def bookInfo(request, pk):
    books = Book.objects.get(id=pk)
    return render(request, "books/book-info.html", {
        "books" : books
    })