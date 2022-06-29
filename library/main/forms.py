from django import forms
from django.forms import TextInput, Select
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

from . import models
from .customwidjet import DateSelectorWidget
from .models import Book, ImageBook, PersonReader, Author, Genre


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookFormGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
    # name = forms.CharField(max_length=100, label='Жанр')


class BookFormAuthors(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ImageBookForm(forms.ModelForm):
    class Meta:
        model = ImageBook
        fields = '__all__'


class PersonReaderForm(forms.ModelForm):
    class Meta:
        model = PersonReader
        fields = '__all__'

        widgets = {
            'date_birthday': DateSelectorWidget,
        }


class Author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
