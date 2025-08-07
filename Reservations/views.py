from Books.models import book
from django.shortcuts import render, redirect
from .forms import contactForm2
from django.contrib import messages
from django.urls import reverse

def reservation_page(response):
    if response.method == 'POST':
        form = contactForm2(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'رزرو با موفقیت ثبت شد! ')
            return redirect(reverse('book_page'))
    else:
        form = contactForm2()
    
    return render(response, 'Reservations/index1.html', {'form': form})
# Create your views here.