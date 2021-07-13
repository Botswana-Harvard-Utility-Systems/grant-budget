from django.db import models
from .dept_budget import DepartmentBudget


class Budget(models.Model):
    department_budgets = models.ForeignKey(DepartmentBudget, on_delete=models.CASCADE)

