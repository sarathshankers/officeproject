from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView
from employee.models import Departments,Employees
from employee.forms import DepartmentForm,EmployeeForm
from django.urls import reverse_lazy


class DepartmentView(CreateView):
    template_name = 'add_dep.html'
    model = Departments
    form_class = DepartmentForm
    success_url = reverse_lazy('add_dep')

    def get(self,request,*args,**kwargs):
        alldep = self.model.objects.all()
        context={'alldep': alldep,'form':self.form_class}
        return render(request,self.template_name,context)

class EmployeeView(CreateView):
    template_name = 'add_emp.html'
    model = Employees
    form_class = EmployeeForm
    success_url = reverse_lazy('add_emp')

    def get(self,request,*args,**kwargs):
        allemp=self.model.objects.all()
        context={'allemp':allemp,'form':self.form_class}
        return render(request,self.template_name,context)


def deletedeprtmnt(request,*args,**kwargs):
    depratment_id=kwargs.get('dep_id')
    qs=Departments.objects.get(id=depratment_id)
    qs.delete()
    return redirect('add_dep')

class EditdeprtmntView(UpdateView):
    form_class = DepartmentForm
    model = Departments
    template_name = 'edit_dep.html'
    pk_url_kwarg = 'dep_id'
    success_url = reverse_lazy('add_dep')

def deleteemployee(request,*args,**kwargs):
    emp_id=kwargs.get('emp_id')
    qs=Employees.objects.get(id=emp_id)
    qs.delete()
    return redirect('add_emp')

class EditEmpView(UpdateView):
    form_class = EmployeeForm
    model = Employees
    template_name = 'edit_emp.html'
    pk_url_kwarg = 'emp_id'
    success_url = reverse_lazy('add_emp')