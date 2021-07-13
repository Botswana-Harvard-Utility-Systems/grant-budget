from django.contrib import admin
from ..models import Budget
from ..forms import BudgetForm
from ..main_admin import grand_budget_admin


@admin.register(Budget, site=grand_budget_admin)
class BudgetAdmin(admin.ModelAdmin):
    form = BudgetForm
