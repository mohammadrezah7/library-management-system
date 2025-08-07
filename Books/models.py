from django.db import models

class book(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    author = models.CharField(max_length=300, verbose_name='author')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='published_date')
    is_availabe = models.BooleanField(default=True, verbose_name='available/not available')

    def __str__(self):
        return f'{self.title}'
# Create your models here.
