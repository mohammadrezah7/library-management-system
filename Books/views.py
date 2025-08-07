from django.shortcuts import render

def book_page(response):
    return render(response, 'Book/index2.html')

# Create your views here.
