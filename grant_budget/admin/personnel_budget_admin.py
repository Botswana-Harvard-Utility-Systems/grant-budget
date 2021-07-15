from django.contrib import admin
from ..models import PersonnelBudget
from ..forms import PersonnelBudgetForm
from ..main_admin import grand_budget_admin


@admin.register(PersonnelBudget, site=grand_budget_admin)
class PersonnelAdmin(admin.ModelAdmin):
    form = PersonnelBudgetForm
