from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import os

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('', filename)
    
class Product(models.Model):
    Fu = 'fund'
    Se = 'sell'
    my_choices = (
            (Fu, 'Fund'),
            (Se, 'Sell'),)
    p_id = models.IntegerField()
    name = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.FileField(upload_to = get_image_path, blank = True, null = True)
    unitcost = models.IntegerField()
    fund_or_sell = models.CharField(choices = my_choices, max_length = 25)
    video_url = models.URLField(default = None)
    manfac_id = models.IntegerField()
    
    def __str__(self):
        return self.name        

   
