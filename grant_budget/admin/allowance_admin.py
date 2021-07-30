from django.contrib import admin
from ..models import Allowance
from ..forms import AllowanceForm
from ..admin_site import grant_budget_admin


@admin.register(Allowance, site=grant_budget_admin)
class AllowanceAdmin(admin.ModelAdmin):
    form = AllowanceForm
