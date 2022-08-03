from django import forms
from employee.models import Employees,Departments

class DepartmentForm(forms.ModelForm):
   class Meta:
       model=Departments
       fields='__all__'



class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields='__all__'