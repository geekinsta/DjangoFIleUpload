from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='book_home'),
    path('create/', create_book, name='book_create'),
]