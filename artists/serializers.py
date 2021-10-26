from rest_framework import serializers
from .models import Artist, Member


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Artist
        # the fields to include in the serialization
        fields = "__all__"


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Member
        # the fields to include in the serialization
        fields = "__all__"
