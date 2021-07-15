from django.db import models

from edc_base.model_mixins import BaseUuidModel


class StaffingBudget(BaseUuidModel):

    # department_budgets = models.ForeignKey(DepartmentBudget, on_delete=models.CASCADE)
    fte = models.FloatField()
    duration = models.IntegerField()

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Grand Budget'
        verbose_name_plural = 'Grant Budget'
