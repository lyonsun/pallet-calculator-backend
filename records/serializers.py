from rest_framework import serializers
from .models import Record
from pallets.models import Pallet

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
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