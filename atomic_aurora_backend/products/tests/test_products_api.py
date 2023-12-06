from django.urls import reverse
from rest_framework import status


class TestProductsAPI:
    products_url = reverse("api:product-list")

    def test_can_get_products(self, products, unauthenticated_client):
        """Should be able to get a list of available products with a get request."""
        response = unauthenticated_client.get(self.products_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert len(data) > 0
        assert len(data) == len(products)

    def test_products_have_price(self, products, unauthenticated_client):
        """products returned in a get request should have a price"""
        response = unauthenticated_client.get(self.products_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data[0]["price"] > 0

    def test_products_have_pictures(self, products_with_pictures, unauthenticated_client):
        """products returned in a get request should have a price"""
        response = unauthenticated_client.get(self.products_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert len(data[0]["pictures"]) > 0
        pic = data[0]["pictures"][0]
        print(pic)
        assert pic["description"]
        assert pic["picture"]

    def test_products_have_name(self, products, unauthenticated_client):
        """products returned in a get request should have a price"""
        response = unauthenticated_client.get(self.products_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data[0]["name"]

    def test_products_have_description(self, products, unauthenticated_client):
        """products returned in a get request should have a price"""
        response = unauthenticated_client.get(self.products_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data[0]["description"]

    def test_products_have_kind(self, products, unauthenticated_client):
        """products returned in a get request should have a price"""
        response = unauthenticated_client.get(self.products_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data[0]["kind"]

    def test_products_have_color(self, product_with_color, unauthenticated_client):
        """products returned in a get request should have a price"""
        response = unauthenticated_client.get(self.products_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data[0]["color"]
