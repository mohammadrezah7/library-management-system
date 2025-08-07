from django.db import models
from Books.models import book

class reservations(models.Model):
    available_books = book.objects.filter(is_availabe=True)
    list_books = []
    for i in available_books:
        a = (i.title.upper(), f'{i.title}')
        list_books.append(a)
        a = ()
    reserver_name = models.CharField(max_length=300, verbose_name='reserver_name', default="")
    book_reserver = models.CharField(max_length=300, choices=list_books, default=list_books[0][0])
    reserver_time = models.DateTimeField(auto_now_add=True, verbose_name='reserver_time', null=True)
# Create your models here.