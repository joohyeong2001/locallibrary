from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count() 
    num_authors = Author.objects.count()
    num_genre = Genre.objects.filter(name__iexact='nOvEL').count()
    num_books_matilda = Book.objects.filter(title__iexact='maTilDa').count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_books_matilda': num_books_matilda,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book