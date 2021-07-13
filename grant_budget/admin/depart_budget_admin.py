from django.contrib import admin
from ..models import DepartmentBudget, Budget
from ..forms import DepartmentBudgetForm
from ..main_admin import grand_budget_admin


# @admin.register(Budget, site=grand_budget_admin)
class BudgetAdmin(admin.TabularInline):
    model = Budget


@admin.register(DepartmentBudget, site=grand_budget_admin)
class DepartmentBudgetAdmin(admin.ModelAdmin):
    form = DepartmentBudgetForm
    inlines = [BudgetAdmin, ]
