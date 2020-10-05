from django.db import models
from pallets.models import Pallet

class Record(models.Model):
    username = models.CharField(max_length=30)
    box_number = models.CharField(max_length=100)
    article_name = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100)
    amount = models.IntegerField()
    record_time = models.TimeField()
    registration_date = models.DateField()
    due_date = models.DateField()
    pallet = models.ForeignKey(Pallet, on_delete=models.CASCADE)