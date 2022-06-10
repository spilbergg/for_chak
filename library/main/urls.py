from django.urls import path

from .views import page_index, image_add, main_page

app_name = 'lib'

urlpatterns = [
    path('register_book/', page_index, name='page_index'),
    path('image_add/',image_add, name='image_add'),
    path('', main_page, name='main_page'),
]
