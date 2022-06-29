from django.shortcuts import render, redirect
from django.template.defaulttags import url

from .forms import BookForm, ImageBookForm, PersonReaderForm, Author_form, BookFormGenre, BookFormAuthors

from .models import Book, ImageBook, PersonReader



def page_index(request):
    form = BookForm()
    form_genre = BookFormGenre()
    form_authors = BookFormAuthors()
    context = {
        'form': form,
        'form_genre': form_genre,
        'form_authors': form_authors
    }
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            ImageBook.objects.create(photo_book=request.FILES['image'], books=book)
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
            }
    return render(request, 'page_index.html', context)


def book_genre_popup_add(request):
    if request.method == 'POST':
        form1 = BookFormGenre(request.POST)
        if form1.is_valid():
            form1.save()

    return redirect('lib:page_index')


def book_author_popup_add(request):

    if request.method == 'POST':
        form1 = BookFormAuthors(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
    return redirect('lib:page_index')



def image_add(request):
    form = ImageBookForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ImageBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
            }
    return render(request, 'image_add.html', context)


def main_page(request):
    books = Book.objects.all()
    print(dir(Book))
    context={
        'books':books,
    }
    return render(request, 'main_page.html', context)


def add_reader(request):
    form = PersonReaderForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PersonReaderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
            }
    return render(request, 'person_form.html', context)


def add_author(request):
    form = Author_form()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = Author_form(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
            }
    return render(request, 'author_form.html', context)

def readers_page(request):
    readers = PersonReader.objects.all()
    context = {
        'readers':readers
    }
    return render(request, 'reades_page.html', context)
