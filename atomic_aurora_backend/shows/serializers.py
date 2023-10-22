from rest_framework import serializers

from atomic_aurora_backend.pictures.serializers import PictureSerializer
from atomic_aurora_backend.shows.models import Show


class ShowSerializer(serializers.ModelSerializer[Show]):
    pictures = PictureSerializer(many=True)

    class Meta:
        model = Show
        fields = "__all__"
