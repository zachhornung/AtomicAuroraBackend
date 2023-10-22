from rest_framework import serializers

from atomic_aurora_backend.pictures.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"
