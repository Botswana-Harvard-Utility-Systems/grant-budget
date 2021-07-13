from django.db import models
from bhp_personnel.models import Department


class DepartmentBudget(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
