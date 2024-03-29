from django.urls import path
from .views import index, AlbumListView, AlbumDetailView

urlpatterns = [
    path("", AlbumListView.as_view(), name="album-list"),
    path("<int:id>/", AlbumDetailView.as_view(), name="album-detail"),
    path("view/", index),
]
