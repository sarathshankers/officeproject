from django.urls import path
from employee import views

urlpatterns = [
    path('department/addnew',views.DepartmentView.as_view(),name='add_dep'),
    path('employee/addnew',views.EmployeeView.as_view(),name='add_emp'),
    path('department/delete/<int:dep_id>',views.deletedeprtmnt,name='del_dep'),
    path('department/edit/<int:dep_id>',views.EditdeprtmntView.as_view(),name='edit_dep'),
    path('emp/delete/<int:emp_id>',views.deleteemployee,name='delete_emp'),
    path('employee/edit/<int:emp_id>',views.EditEmpView.as_view(),name='edit_emp'),


]