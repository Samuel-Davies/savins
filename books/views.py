from django.shortcuts import render

# Create your views here.

def chooseBook(request):
    return render(request, 'books/choose-book.html')