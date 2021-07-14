from django.db import models


class Grant(models.Model):
    pi = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
