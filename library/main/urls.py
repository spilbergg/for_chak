from django.urls import path

from .views import page_index, image_add, main_page,add_reader,add_author

app_name = 'lib'

urlpatterns = [
    path('register_book/', page_index, name='page_index'),
    path('image_add/',image_add, name='image_add'),
    path('', main_page, name='main_page'),
    path('add_reader/',add_reader, name='add_reader'),
    path('add_author', add_author, name='add_author')
]
