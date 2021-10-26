from django.urls import path
from .views import index, AlbumListView, AlbumDetailView

urlpatterns = [
    path("", AlbumListView.as_view()),
    path("<int:id>/", AlbumDetailView.as_view()),
    path("view/", index),
]
