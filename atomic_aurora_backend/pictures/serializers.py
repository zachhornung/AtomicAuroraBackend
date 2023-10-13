from atomic_aurora_backend.pictures.models import Picture
from rest_framework import serializers

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"
