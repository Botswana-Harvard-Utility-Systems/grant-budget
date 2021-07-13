from django.db import models
from bhp_personnel.models import Department
from .grant import Grant


class DepartmentBudget(models.Model):
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
