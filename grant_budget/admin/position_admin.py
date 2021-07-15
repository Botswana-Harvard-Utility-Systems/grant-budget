from django.contrib import admin
from ..models import Position
from ..forms import PositionForm
from ..main_admin import grand_budget_admin


@admin.register(Position, site=grand_budget_admin)
class PositionAdmin(admin.ModelAdmin):

    form = PositionForm
