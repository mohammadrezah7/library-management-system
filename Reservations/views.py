from django.shortcuts import render, redirect
from .forms import contactForm2
from django.contrib import messages
from django.urls import reverse
from Books.models import book

def reservation_page(response):
    available = book.objects.all()
    if response.method == 'POST':
        form = contactForm2(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'رزرو با موفقیت ثبت شد! ')
            name1 = response.POST.get('book_reserver')
            for i in available:
                if i.title == name1:
                    i.is_availabe = False
                    i.save()
            return redirect(reverse('book_page'))
    else:
        form = contactForm2()
        
    return render(response, 'Reservations/index1.html', {'form': form})
# Create your views here.