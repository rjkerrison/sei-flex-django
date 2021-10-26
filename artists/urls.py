from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSet, MemberViewSet

router = routers.DefaultRouter()
router.register("artists", ArtistViewSet)
router.register("members", MemberViewSet)

urlpatterns = [path("", include(router.urls))]
