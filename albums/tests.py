from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from albums.models import Album


class AlbumTests(APITestCase):
    def test_create_album(self):
        """
        Ensure we can create a new album object via the API.
        """

        # Grab the URL based on its name (check this matches albums/urls.py)
        url = reverse("album-list")
        # Define some data that we can build our test around
        data = {
            "title": "I See You",
            "artist": {
                "name": "The xx",
            },
            "cover_image": "https://placeholder.it/300x300",
        }
        # Execute the test case (this is boilerplate)
        response = self.client.post(url, data, format="json")

        # First: check the request didn't error
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Second: check we created an album
        self.assertEqual(Album.objects.count(), 1)

        created_album = Album.objects.get()
        # Check the album title
        self.assertEqual(created_album.title, "I See You")
        # Check we added its artist
        self.assertIsNotNone(created_album.artist)
        # Check we gave the artist the right name
        self.assertEqual(created_album.artist.name, "The xx")

    def test_update_album(self):
        """
        Ensure we can update an album via the API.
        """
        # somebody already created it as "The White Album" and we need to set things straight
        url = reverse("album-detail", args=[1])
        data = {
            "title": "The Beatles",
            "artist": "The Beatles",
            "cover_image": "https://placeholder.it/300x300",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 1)
        self.assertEqual(Album.objects.get().title, "I See You")
        self.assertEqual(Album.objects.get().artist, "The xx")
