import pytest

from rest_framework.reverse import reverse
from rest_framework import status

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
