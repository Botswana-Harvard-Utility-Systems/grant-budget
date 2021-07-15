from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_base.model_mixins import BaseUuidModel
from bhp_personnel.models.employee import Employee


class Salary(BaseUuidModel):
    employee = models.OneToOneField(
        Employee,
        verbose_name="Employee",
        on_delete=models.CASCADE)

    gross_salary = models.DecimalField(
        verbose_name="Gross Salary",
        validators=[MinValueValidator(1), ],
        max_digits=10,
        decimal_places=2)

    pension = models.DecimalField(
        verbose_name="Pension",
        validators=[MinValueValidator(1), ],
        max_digits=10,
        decimal_places=2)

    def __str__(self):
        return f"{self.gross_salary}"

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Grand Budget'
        verbose_name_plural = 'Grant Budget'
