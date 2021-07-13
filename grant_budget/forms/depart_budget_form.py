from django import forms
from ..models import DepartmentBudget


class DepartmentBudgetForm(forms.ModelForm):
    class Meta:
        model = DepartmentBudget
        fields = '__all__'
