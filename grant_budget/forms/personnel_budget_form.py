from django import forms
from ..models import PersonnelBudget


class PersonnelBudgetForm(forms.ModelForm):
    class Meta:
        model = PersonnelBudget
        fields = '__all__'
