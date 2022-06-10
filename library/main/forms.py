from django import forms

from .models import Book, ImageBook, PersonReader,Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ImageBookForm(forms.ModelForm):
    class Meta:
        model = ImageBook
        fields = '__all__'

class PersonReaderForm(forms.ModelForm):
    class Meta:
        model = PersonReader
        fields = '__all__'
        exclude = ['date_birthday']

class Author_form(forms.ModelForm):
    class Meta:
        model =Author
        fields='__all__'
