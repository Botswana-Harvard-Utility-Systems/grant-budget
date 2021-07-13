from django.db import models
from .dept_budget import DepartmentBudget


class Grant(models.Model):
    pi = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
    department_budgets = models.ForeignKey(DepartmentBudget, on_delete=models.CASCADE)
