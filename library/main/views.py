from django.shortcuts import render, redirect
from django.template.defaulttags import url

from .forms import BookForm, ImageBookForm
from .models import Book, ImageBook


def page_index(request):
    form = BookForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            img= ImageBook.objects.create(photo_book=request.FILES['image'], books=book)
            return render(request, 'main_page.html')
    return render(request, 'page_index.html', context)

def image_add(request):
    form= ImageBookForm()
    context={
        'form':form
    }
    if request.method == 'POST':
        form = ImageBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'image_add.html', context)


def main_page(request):
    return render(request, 'main_page.html')