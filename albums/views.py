from django.shortcuts import render
from django.http import HttpResponse

from .models import Album

# Create your views here.
def index(request):
    print(request)

    # grabbing what we need from database
    list = Album.objects.all
    # creating a context object
    context = {"albums": list}

    # rendering based on a template
    return render(request, "albums/index.html", context)


# API handlers
def albums(request):
    if request.method == "GET":
        return read(request)
    if request.method == "POST":
        return create(request)


def album(request):
    if request.method == "GET":
        return read_one(request)
    if request.method == "PATCH":
        return update(request)
    if request.method == "DELETE":
        return delete(request)


# CRUD TIME
def create(request):
    # something something
    return HttpResponse("CREATE")


def read(request):
    # can we get albums back as json?
    return HttpResponse("READ")


def read_one(request):
    # can we get one album back as json?
    return HttpResponse("READ ONE")


def update(request):
    # can we update an album
    return HttpResponse("UPDATE")


def delete(request):
    # can we delete an album
    return HttpResponse("DELETE")
