from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField(default='N/A')
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name
