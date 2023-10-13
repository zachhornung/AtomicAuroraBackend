from rest_framework import serializers

from atomic_aurora_backend.shows.models import Show
from atomic_aurora_backend.pictures.serializers import PictureSerializer


class ShowSerializer(serializers.ModelSerializer[Show]):

    pictures = PictureSerializer(many=True)

    class Meta:
        model = Show
        fields = "__all__"

