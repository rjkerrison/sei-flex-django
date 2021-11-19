from rest_framework import serializers
from .models import Artist, Member


class ArtistLiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Artist
        # the fields to include in the serialization
        fields = (
            "id",
            "name",
            "members",
        )
        depth = 1
