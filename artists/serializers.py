from rest_framework import serializers
from .models import Artist, Member
from albums.serializers import AlbumShallowSerializer


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = AlbumShallowSerializer(many=True, read_only=True)

    class Meta:
        # the model that the serializer is based on
        model = Artist
        # the fields to include in the serialization
        fields = (
            "id",
            "name",
            "members",
            "albums",
        )
        depth = 2


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Member
        # the fields to include in the serialization
        fields = (
            "id",
            "name",
            "date_of_birth",
            "artists",
        )
        depth = 1
