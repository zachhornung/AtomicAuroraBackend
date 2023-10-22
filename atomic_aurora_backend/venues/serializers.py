from rest_framework import serializers

from atomic_aurora_backend.venues.models import Venue


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"
