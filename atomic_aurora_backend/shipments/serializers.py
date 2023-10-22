from rest_framework import serializers

from atomic_aurora_backend.shipments.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer[Shipment]):
    class Meta:
        model = Shipment
        fields = "__all__"
