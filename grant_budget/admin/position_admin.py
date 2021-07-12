from django.contrib import admin

from grant_budget.models import FTE, Project
from grant_budget.main_admin import grand_budget_admin


@admin.register(FTE, site=grand_budget_admin)
class FTEModelAdmin(admin.ModelAdmin):
    list_display = [
        'employee',
        'project',
        'current_fte',
        'fte_short',
        'fte_total',
        'project_period'
    ]


@admin.register(Project, site=grand_budget_admin)
class ProjectModelAdmin(admin.ModelAdmin):
    pass
