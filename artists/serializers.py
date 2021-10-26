from rest_framework import serializers
from .models import Artist, Member
from albums.serializers import AlbumShallowSerializer


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    # Important bit: overriding the HyperlinkedModelSerializer's default serializer for a related field
    albums = AlbumShallowSerializer(many=True, read_only=True)

    class Meta:
        # the model that the serializer is based on
        model = Artist
        # the fields to include in the serialization
        fields = (
            "id",
            "name",
            "members",
            # Important bit: these "reverse" relationships weren't included when we had "__all__"
            "albums",
        )
        # Important bit: depth
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
            # Important bit: these "reverse" relationships weren't included when we had "__all__"
            "artists",
        )
        depth = 1
