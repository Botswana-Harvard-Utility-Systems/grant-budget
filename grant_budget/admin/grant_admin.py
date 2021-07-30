from django.contrib import admin
from ..models import Grant
from ..forms import GrantForm
from ..admin_site import grant_budget_admin


@admin.register(Grant, site=grant_budget_admin)
class GrantAdmin(admin.ModelAdmin):
    form = GrantForm
