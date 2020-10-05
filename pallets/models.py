from django.db import models

# Create your models here.
class Pallet(models.Model):
    pallet_id = models.CharField(max_length=100, unique=True)
    total_boxes = models.IntegerField()
    updated_at = models.DateTimeField()
