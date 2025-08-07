from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_page, name='book_page'),
]