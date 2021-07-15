from django.contrib import admin
from ..models import PersonalBudget
from ..forms import PersonnelBudgetForm
from ..main_admin import grand_budget_admin


@admin.register(PersonalBudget, site=grand_budget_admin)
class PersonnelAdmin(admin.ModelAdmin):

    form = PersonnelBudgetForm
