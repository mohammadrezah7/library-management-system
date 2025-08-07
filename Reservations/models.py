from django.db import models
from django.utils.functional import lazy
from Books.models import book

def get_book_choices():
    available_books = book.objects.filter(is_availabe=True)
    list_books = []
    for i in available_books:
        a = (i.title.upper(), f'{i.title}')
        list_books.append(a)
        a = ()
    return list_books

class reservations(models.Model):
    reserver_name = models.CharField(max_length=300, verbose_name='reserver_name', default="")
    book_reserver = models.CharField(max_length=300, choices=lazy(get_book_choices, list)(),default="")
    reserver_time = models.DateTimeField(auto_now_add=True, verbose_name='reserver_time', null=True)