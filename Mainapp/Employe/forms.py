# from django import forms
# from .models import Employees




from django import forms 
from.models import Employees

class EmployeesForm(forms.ModelForm):
    class Meta:
        model=Employees
        exclude= ['id','date_added','date_updated']











