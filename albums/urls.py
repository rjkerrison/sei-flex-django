from django.urls import path
from .views import index, AlbumListView, AlbumDetailView

urlpatterns = [
    path("", index),
    path("api/", AlbumListView.as_view()),
    path("api/<int:id>/", AlbumDetailView.as_view()),
]
