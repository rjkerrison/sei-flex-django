from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import views, response, status

from .models import Album
from .serializers import AlbumSerializer

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
        serialized_albums = AlbumSerializer(albums, many=True)
        return response.Response(serialized_albums.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        # create an Album instance from the request data
        album_to_add = AlbumSerializer(data=request.data)
        # save the Album to database
        if album_to_add.is_valid():
            album_to_add.save()
            return response.Response(album_to_add.data, status=status.HTTP_201_CREATED)

        return response.Response(
            album_to_add.errors, status=status.HTTP_400_BAD_REQUEST
        )
