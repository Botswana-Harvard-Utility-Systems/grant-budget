from django.contrib import admin
from ..models import Salary
from ..forms import SalaryForm
from ..main_admin import grand_budget_admin


@admin.register(Salary, site=grand_budget_admin)
class SalaryAdmin(admin.ModelAdmin):
    form = SalaryForm
