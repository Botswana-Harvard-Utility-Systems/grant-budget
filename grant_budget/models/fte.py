from django.db import models
from dateutil import relativedelta
from .project import Project
from .employee import Employee


class FTE(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    current_fte = models.FloatField()

    # start = models.DateField()
    # end = models.DateField()

    @property
    def fte_total(self):
        ftes = FTE.objects.filter(employee=self.employee)
        total = 0.0
        for fte in ftes:
            total += fte.current_fte
        return total

    @property
    def fte_short(self):
        if self.fte_total > 100.0:
            return 100 - self.fte_total
        else:
            return 0

    @property
    def project_period(self):
        months = relativedelta.relativedelta(self.project.end, self.project.start).months
        return f'{months} month(s)'

    class Meta:
        verbose_name = 'FTE'
        verbose_name_plural = 'FTE'
