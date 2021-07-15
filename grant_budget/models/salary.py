from django.db import models
from edc_base.model_mixins import BaseUuidModel
from bhp_personnel.models.employee import Employee


class Salary(BaseUuidModel):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE
    )

    gross_salary = models.DecimalField(
        verbose_name="Gross Salary",
        max_length=10,
        decimal_places=2
    )

    pension = models.DecimalField(
        verbose_name="Pension",
        max_length=10,
        decimal_places=2
    )
