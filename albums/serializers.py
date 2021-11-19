from rest_framework import serializers
from .models import Album
from artists.lite_serializers import ArtistLiteSerializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistLiteSerializer()

    class Meta:
        # the model that the serializer is based on
        model = Album
        # the fields to include in the serialization
        fields = (
            "title",
            "cover_image",
            "artist",
        )
        # extra_kwargs = {
        #     "artist_name": {
        #         "required": True,
        #     },
        # }
        # Important bit: the depth adds related fields' information into the response
        depth = 1

    # We override validation
    def validate(self, attrs):
        # We can do whatever validation we like here,
        # but in this case (to keep it simple) we'll just accept anything
        return attrs

    def create(self, validated_data):
        print(validated_data)
        artist = validated_data.pop("artist")

        print("{0:-50}".format(artist.name))

        print(user, validated_data)

        album = Album.objects.create(
            user=user,
            has_checked_out=False,
            check_in_time=datetime.datetime.now(),
        )

        check_in.save()

        return check_in


class AlbumShallowSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Album
        # the fields to include in the serialization
        fields = "__all__"
        depth = 0
