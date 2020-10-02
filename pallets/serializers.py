from rest_framework import serializers
from .models import Pallet

class PalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pallet
        fields = [
            'pallet_id',
            'username',
            'box_number',
            'article_name',
            'batch_number',
            'amount',
            'record_time',
            'registration_date',
            'due_date',
            'updated_at'
        ]