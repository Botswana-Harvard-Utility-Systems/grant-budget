from django import forms
from ..models import Allowance


class AllowanceForm(forms.ModelForm):
    class Meta:
        model = Allowance
        fields = '__all__'
