from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Album
        # the fields to include in the serialization
        fields = "__all__"