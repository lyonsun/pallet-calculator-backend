from rest_framework import serializers
from .models import Record
from pallets.models import Pallet
from pallets.serializers import PalletSerializer

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'id',
            'username',
            'box_number',
            'article_name',
            'batch_number',
            'amount',
            'record_time',
            'registration_date',
            'due_date',
            'pallet'
        ]

    def to_representation(self, instance):
        self.fields['pallet'] = PalletSerializer(read_only=True)
        return super(RecordSerializer, self).to_representation(instance)