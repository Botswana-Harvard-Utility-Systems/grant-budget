from django.contrib import admin
from ..models import DepartmentBudget
from ..forms import DepartmentBudgetForm
from ..main_admin import grand_budget_admin


@admin.register(DepartmentBudget, site=grand_budget_admin)
class DepartmentBudgetAdmin(admin.ModelAdmin):
    form = DepartmentBudgetForm
