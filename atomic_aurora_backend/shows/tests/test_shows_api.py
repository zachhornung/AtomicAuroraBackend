import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestShowsAPI:
    shows_list_url = reverse("api:show-list")

    def test_can_get_list_of_shows(self, shows, unauthenticated_client):
        response = unauthenticated_client.get(self.shows_list_url)
        assert response.status_code == status.HTTP_200_OK
        actual_shows = response.json()
        print("actualk shows: ", actual_shows)
        actual_show_pks = [s.get("id") for s in actual_shows]

        assert len(actual_shows) == len(shows)
        assert all(show.pk in actual_show_pks for show in shows)

    @pytest.mark.django_db
    def test_cant_create_show(self, unauthenticated_client):
        """
        shouldnt be able to create a show via api
        """
        response = unauthenticated_client.post(self.shows_list_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_cant_modify_show(self, show, unauthenticated_client):
        """
        modifying shows via api should not be possible
        """
        response = unauthenticated_client.put(show.get_absolute_url())
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    @pytest.mark.django_db
    def test_shows_return_pictures(self, unauthenticated_client, show_with_picture):
        """
        Shows should return any pictures that they have
        """
        response = unauthenticated_client.get(show_with_picture.get_absolute_url())
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        expected_picture_description = show_with_picture.pictures.first().description
        actual_picture_description = data.get("pictures")[0]["description"]
        assert actual_picture_description == expected_picture_description
