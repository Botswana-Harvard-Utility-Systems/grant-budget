from django.db import models

from edc_base.model_mixins import BaseUuidModel
from grant_budget.models.personal_budget import DepartmentBudget


class StaffingBudget(BaseUuidModel):

    department_budgets = models.ForeignKey(DepartmentBudget, on_delete=models.CASCADE)
    fte = models.FloatField()
    duration = models.IntegerField()

