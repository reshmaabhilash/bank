from django import forms
from bankapp.models import Userform,Branch
class BankForm(forms.ModelForm):
    class Meta:
        model=Userform
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset= Branch.objects.all()