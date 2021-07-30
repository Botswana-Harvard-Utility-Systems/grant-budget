from django.contrib import admin
from ..models import PersonnelBudget
from ..forms import PersonnelBudgetForm
from ..admin_site import grant_budget_admin


@admin.register(PersonnelBudget, site=grant_budget_admin)
class PersonnelAdmin(admin.ModelAdmin):
    form = PersonnelBudgetForm
