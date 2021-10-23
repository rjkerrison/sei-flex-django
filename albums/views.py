from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import views, response, status

from .models import Album

# Create your views here.
def index(request):
    # grabbing what we need from database
    list = Album.objects.all()
    # creating a context object
    context = {"albums": list}

    # rendering based on a template
    return render(request, "albums/index.html", context)


class AlbumListView(views.APIView):
    def get(self, request):
        albums = Album.objects.all()
        return response.Response(albums, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        return response.Response("POST!", status=status.HTTP_201_CREATED)
