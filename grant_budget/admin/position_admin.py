from django.contrib import admin
from ..models import Position
from ..forms import PositionForm
from ..admin_site import grant_budget_admin


@admin.register(Position, site=grant_budget_admin)
class PositionAdmin(admin.ModelAdmin):
    form = PositionForm
