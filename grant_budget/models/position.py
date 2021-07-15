from django.db import models
from edc_base.model_mixins import BaseUuidModel


class Position(BaseUuidModel):

    name = models.CharField(
        verbose_name="Name of the Position",
        max_length=50,
        blank=True,
        null=True)

    est_ctc = models.FloatField(
        verbose_name="Average Estimated cost to company",
        max_length=50,
        blank=True,
        null=True)

    salary_range_lower = models.FloatField(
        verbose_name="Salary range lower amouunt",
        max_length=50,
        blank=True,
        null=True)

    salary_range_upper = models.FloatField(
        verbose_name="Salary range upper amouunt",
        max_length=50,
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Grand Budget'
        verbose_name_plural = 'Grant Budget'
