from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.

def index(request):
    return HttpResponse("Test URL")

# returns titles of every book
def bookTitle(request):
    titles = ""
    everybook = Book.objects.all()

    for eachElement in everybook:
        titles += eachElement.name + "<br>"

    return HttpResponse(titles)

# Filters out books after specific publish date
def pub2018OrByond(request):
    books2018AndOver = Book.objects.filter(publishDate__gte='2018-01-01')
    return HttpResponse(books2018AndOver)

#Attempted to get it to work but it doesn't from what I could do with the time I had.
def updateGenre(request):
    changeFiction = Book.objects.filter(publishDate__gte='2018-01-01')
    changeFiction = changeFiction[0]
    changeFiction[0].genre = "Fiction"
    changeFiction[0].save()
