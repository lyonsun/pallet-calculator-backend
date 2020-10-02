from django.db import models

# Create your models here.
class Pallet(models.Model):
    pallet_id = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    box_number = models.CharField(max_length=100)
    article_name = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100)
    amount = models.IntegerField()
    record_time = models.TimeField()
    registration_date = models.DateField()
    due_date = models.DateField()
    updated_at = models.DateTimeField()
