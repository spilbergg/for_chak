from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    name_book_rus = models.CharField(max_length=100, verbose_name='Название книги')
    name_book_origin = models.CharField(max_length=100, null=True, blank=True, verbose_name='Оригинальное название')
    genre_book = models.ManyToManyField('Genre')
    price_book = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    count_book = models.IntegerField(verbose_name='Количество')
    all_author_book = models.ManyToManyField('Author', verbose_name='Все авторы книги')
    price_one_day_period = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Стоимость одного дня')
    year_published = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(2100),
                                                                            MinValueValidator(1200)],
                                         verbose_name='Год выпуска')
    date_register_book_in_database = models.DateField(auto_now_add=True, verbose_name='Дата регистрации книги')
    count_page_book = models.IntegerField(null=True, blank=True, verbose_name='Количество страниц')

    def __str__(self):
        return self.name_book_rus


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='')
    last_name = models.CharField(max_length=50, verbose_name='')
    foto_author = models.ImageField(upload_to='images', verbose_name='Фотография автора')

    def __str__(self):
        return self.last_name


class Genre(models.Model):
    name_genre = models.CharField(max_length=30)

    def __str__(self):
        return self.name_genre


class ImageBook(models.Model):
    photo_book = models.ImageField(upload_to='images', verbose_name='Фотография обложки книги')
    books = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='книги')

    def __str__(self):
        return 'фотографии книг'


class PersonReader(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Фамилия')
    last_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=True)
    number_passport = models.CharField(max_length=9, verbose_name='Отчество', unique=True)
    date_birthday = models.DateField(verbose_name='дата рождения')
    email = models.EmailField(verbose_name='Email')
    residential_address = models.CharField(max_length=100, verbose_name='Адрес проживания', null=True)

    def __str__(self):
        return self.first_name

