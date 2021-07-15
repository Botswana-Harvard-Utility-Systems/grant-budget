from django.db import models
from edc_base.model_mixins import BaseUuidModel


class Allowance(BaseUuidModel):
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
