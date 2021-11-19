from django.shortcuts import render
from rest_framework import viewsets

from .models import Artist, Member
from .serializers import ArtistSerializer, MemberSerializer

# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
