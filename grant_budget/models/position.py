from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=50)
    est_ctc = models.FloatField()
