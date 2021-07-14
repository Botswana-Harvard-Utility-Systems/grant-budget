from django.db import models

from edc_base.model_mixins import BaseUuidModel

from .staffing_budget import StaffingBudget


class PersonalBudget(BaseUuidModel):
    
    # TODO: add the cascade...on the foreign key
    staffing_budget = models.ForeignKey(StaffingBudget, )


    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'grant_budget'
        verbose_name = 'Personal Budget'
        verbose_name_plural = 'Personal Budget'
