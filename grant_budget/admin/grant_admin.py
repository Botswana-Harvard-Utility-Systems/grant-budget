from django.contrib import admin
from ..models import Grant
from ..forms import GrantForm
from ..main_admin import grand_budget_admin


@admin.register(Grant, site=grand_budget_admin)
class GrantAdmin(admin.ModelAdmin):

    form = GrantForm
