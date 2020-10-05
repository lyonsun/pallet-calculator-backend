from rest_framework import serializers
from .models import Pallet

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pallet
        fields = [
            'id',
            'pallet_id',
            'total_boxes',
            'updated_at'
        ]