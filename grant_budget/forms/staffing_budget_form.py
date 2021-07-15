from django import forms
from ..models import StaffingBudget


class StuffingBudgetForm(forms.ModelForm):
    class Meta:
        model = StaffingBudget
        fields = '__all__'

