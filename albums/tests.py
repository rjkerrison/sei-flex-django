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
            "artist_name": "The xx",
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
