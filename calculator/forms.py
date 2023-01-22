from django import forms
from .models import CalcFunding


class CalcFundingForm(forms.ModelForm):
    class Meta:
        model = CalcFunding
        exclude = ()

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'cost': 'Cost',
            'savings': 'Savings',
            'salary_pre': 'Salary before taxes',
            'salary_post': 'Salary afret taxes',
            'expences': 'Monthly expences',
            'fund': 'Funding choice',
        }