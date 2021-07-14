from django.db import models

from edc_base.model_mixins import BaseUuidModel


class Grant(BaseUuidModel):

    pi = models.CharField(
        verbose_name="PI name",
        max_length=50,
        null=True,
        blank=True)

    name = models.CharField(
        verbose_name="Name of the grant",
        max_length=50,
        null=True,
        blank=True)

    start = models.DateField(
        verbose_name="Grant start date",
        null=True,
        blank=True)

    end = models.DateField(
        verbose_name="Grant end date",
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.name} {self.pi}'

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Grand Budget'
        verbose_name_plural = 'Grant Budget'
