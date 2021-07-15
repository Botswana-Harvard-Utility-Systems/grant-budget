from django.db import models
from edc_base.model_mixins import BaseUuidModel
from .salary import Salary


class Allowance(BaseUuidModel):
    salary = models.ForeignKey(
        Salary,
        verbose_name='Salary',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name="Name",
        max_length=10,
        decimal_places=2
    )

    amount = models.DecimalField(
        verbose_name="Amount",
        max_length=10,
        decimal_places=2
    )
