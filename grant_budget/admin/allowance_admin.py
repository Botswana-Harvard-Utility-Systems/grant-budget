from django.contrib import admin
from ..models import Allowance
from ..forms import AllowanceForm
from ..main_admin import grand_budget_admin


@admin.register(Allowance, site=grand_budget_admin)
class AllowanceAdmin(admin.ModelAdmin):
    form = AllowanceForm
