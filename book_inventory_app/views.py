from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from .models import Book

# Create your views here.
def home(request):
  #return HttpResponse('Home Page')
  context = {}
  return render(request, 'index.html', context)

def booksList(request):
  context = {"books": Book.objects.all()}
  return render(request, 'booklist.html', context)

def bookView(request, pk):
  book = get_object_or_404(Book, pk=pk)
  context = {"book": book}
  return render(request, 'bookdetail.html', context)

def redirect_me(self):
  return redirect(reverse('book-list'))