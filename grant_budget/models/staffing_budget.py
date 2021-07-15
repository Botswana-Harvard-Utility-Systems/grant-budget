from django.db import models

from edc_base.model_mixins import BaseUuidModel
from .grant import Grant


class StaffingBudget(BaseUuidModel):
    grant = models.ForeignKey(
        Grant,
        verbose_name="Department Budgets",
        on_delete=models.CASCADE)

    fte = models.FloatField(
        verbose_name="FTE",
        help_text="FTE in should be in (%)")

    duration = models.IntegerField(
        verbose_name="Duration",
        help_text="Duration in months")

    def __str__(self):
        return f"{self.grant}"

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Grand Budget'
        verbose_name_plural = 'Grant Budget'
