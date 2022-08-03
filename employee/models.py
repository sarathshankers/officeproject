from django.db import models

class Departments(models.Model):
    department_name=models.CharField(max_length=50,unique=True)
    department_code=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.department_name

class Employees(models.Model):
    department=models.ForeignKey(Departments,on_delete=models.CASCADE,related_name='dep')
    emp_name=models.CharField(max_length=50)
    emp_email=models.CharField(max_length=50,unique=True)
    emp_phone=models.CharField(max_length=50,unique=True)
    emp_designation=models.CharField(max_length=50)


