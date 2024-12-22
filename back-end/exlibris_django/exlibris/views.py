from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    query = request.GET.get('q', '')  # Get the 'q' parameter from the URL
    if query:
        books = Book.objects.filter(name__icontains=query) | Book.objects.filter(author__name__icontains=query)
    else:
        books = Book.objects.all().order_by('author__name')
    book_count = books.count()
    return render(request, 'book_list.html', {'books': books, 'book_count': book_count})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})