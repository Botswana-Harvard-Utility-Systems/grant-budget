from django.contrib import admin
from ..models import Salary
from ..forms import SalaryForm
from ..admin_site import grant_budget_admin


@admin.register(Salary, site=grant_budget_admin)
class SalaryAdmin(admin.ModelAdmin):
    form = SalaryForm
