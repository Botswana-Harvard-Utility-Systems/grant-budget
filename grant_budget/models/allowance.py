from django.db import models
from edc_base.model_mixins import BaseUuidModel
from .salary import Salary


class Allowance(BaseUuidModel):
    salary = models.ForeignKey(
        Salary,
        verbose_name='Salary',
        on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name="Name",
        max_length=50)

    amount = models.DecimalField(
        verbose_name="Amount",
        max_digits=10,
        decimal_places=2)

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Grand Budget'
        verbose_name_plural = 'Grant Budget'
