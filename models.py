from django.db import models

# Create your models here.
class ckdModel(models.Model):

    MaxHR=models.FloatField()
    ST_Slope_Flat=models.FloatField()
    ST_Slope_Up=models.FloatField()
#    Packed_cell_volume=models.FloatField()
#    White_blood_count=models.FloatField()
