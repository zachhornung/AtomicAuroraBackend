from rest_framework import serializers

from atomic_aurora_backend.shows.models import Show


class ShowSerializer(serializers.ModelSerializer[Show]):
    class Meta:
        model = Show
        fields = "__all__"

