from django.db import models

# Create your models here.
class create(models.Model):
    name = models.CharField(max_length = 30)
    cname = models.CharField( max_length = 10)
    cost =models.CharField( max_length = 50)