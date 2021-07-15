from django.contrib import admin
from ..models import PersonnelBudget
from ..models import StaffingBudget
from ..forms import StuffingBudgetForm
from ..main_admin import grand_budget_admin


class PersonnelBudgetAdmin(admin.TabularInline):
    model = PersonnelBudget


@admin.register(StaffingBudget, site=grand_budget_admin)
class StaffingBudgetAdmin(admin.ModelAdmin):
    form = StuffingBudgetForm

    inlines = [PersonnelBudgetAdmin, ]
