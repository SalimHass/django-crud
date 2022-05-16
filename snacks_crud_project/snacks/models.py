from platform import mac_ver
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    title= models.CharField(max_length=64)
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()

    def __srt__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail_snack', kwargs={"pk":self.pk})


