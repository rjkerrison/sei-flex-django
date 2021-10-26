from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Album
        # the fields to include in the serialization
        fields = "__all__"
        # Important bit: the depth adds related fields' information into the response
        depth = 1


class AlbumShallowSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Album
        # the fields to include in the serialization
        fields = "__all__"
        depth = 0
