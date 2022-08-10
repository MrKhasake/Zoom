from django.shortcuts import render
from .models import Entrepreneurship, Sales, Finance, Contact, News, Slide

# Create your views here.
def index(request):

    slides = Slide.objects.all()
    updates = News.objects.all()
    return render(request, 'index.html', {'slides':slides, 'updates':updates})

def entrepreneur(request):

    post = Entrepreneurship.objects.all()
    return render(request, 'entrepreneurship.html', {'post':post})

def sales(request):
    post = Sales.objects.all()
    return render(request, 'sales.html', {'post':post})

def finance(request):
    post = Finance.objects.all()
    return render(request, 'finance.html', {'post':post})

def contact(request):

    return render(request, 'contact.html')

def check():
    pass
    
def handle_not_found(request, exception):
    return render(request, 'not-found.html')

