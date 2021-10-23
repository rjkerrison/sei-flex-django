from django.urls import path
from .views import index, AlbumListView

urlpatterns = [
    path("", index),
    path("api/", AlbumListView.as_view()),
]
