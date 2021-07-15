from django.db import models
from edc_base.model_mixins import BaseUuidModel
from .staffing_budget import StaffingBudget
from .position import Position


class PersonnelBudget(BaseUuidModel):
    staffing_budget = models.ForeignKey(
        StaffingBudget,
        verbose_name="Staffing Budget",
        on_delete=models.CASCADE)

    position = models.OneToOneField(
        Position,
        verbose_name="Position",
        on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name="Name",
        max_length=50)

    start = models.DateField(verbose_name="Start", )

    end = models.DateField(verbose_name="Start", )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Personnel Budget'
        verbose_name_plural = 'Personnel Budget'
