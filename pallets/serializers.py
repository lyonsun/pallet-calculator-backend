from rest_framework import serializers
from .models import Pallet
from records.serializers import RecordSerializer

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pallet
        fields = [
            'pallet_id',
            'total_boxes',
            'updated_at'
        ]