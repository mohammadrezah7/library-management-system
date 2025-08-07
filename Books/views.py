from django.shortcuts import render, redirect
from .forms import contactForm
from django.contrib import messages
from django.urls import reverse

def book_page(response):
    if response.method == 'POST':
        form = contactForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'اطلاعات با موفقیت ثبت شد!')
            return redirect(reverse('book_page'))
    else:
        form = contactForm()
    
    return render(response, 'Books/index2.html', {'form': form})

# Create your views here.
