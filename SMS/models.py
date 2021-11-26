from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.

class Department(models.Model):
    department_id = models.CharField(
        max_length=10, default='DEPT202100', primary_key=True)
    department_name = models.CharField(max_length=30, default='XYZ', null=True)
    department_manager = models.CharField(max_length=30, default='ABCD', null=True)
    salary_range = models.CharField(max_length=30, default='0000-0000', null=True)


class Employee(models.Model):
    employee_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30 , default= 'XYZ', null=True)
    last_name = models.CharField(max_length=30 , default= 'XYZ', null=True)
    email = models.CharField(max_length=30 , default= 'XYZ@XYZ.XYZ', null=True)
    gender = models.CharField(max_length= 10, default= 'MALE', null=True)
    dob = models.DateField(null=True)
    joining_date = models.DateField(null=True);
    # department_id = models.CharField(
    #     max_length=10, default='DEPT202100')
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

class Employee_address(models.Model):
    # employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    employee_id = models.OneToOneField(
        Employee, on_delete=CASCADE, primary_key=True)

    # employee_id = models.CharField(max_length=10, primary_key=True)    
    state = models.CharField(max_length=50, default='XYZ')
    city = models.CharField(max_length=50, default='XYZ')
    street = models.CharField(max_length=150, default='XYZ')

class Phone_number(models.Model):
    employee_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(
        default=0000000, primary_key=True)

class Administrator(models.Model):
    administrator_id = models.CharField(max_length= 10 , primary_key=True)
    name = models.CharField(max_length=30, default='XYZ')

class Account_detail(models.Model):
    account_number = models.BigIntegerField(primary_key=True, default=00000)
    employee_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    bankname = models.CharField(max_length=50, default='XYZ')
    IFSC_code = models.CharField(max_length=50, default='XYZ') 

class Login(models.Model):
    # employee_id = models.ForeignKey(
    #     Employee, on_delete=models.CASCADE, primary_key=True)
    employee_id = models.OneToOneField(Employee, on_delete=CASCADE, primary_key=True)
    username = models.CharField(max_length=20, default='XYZ')
    password = models.CharField(max_length=20, default='XYZ')

class Transaction(models.Model):
    transaction_id = models.CharField(
        max_length=10, primary_key=True, default='TRAN000000')
    employee_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    net_salary = models.IntegerField()
    account_number = models.ForeignKey(Account_detail, on_delete=models.CASCADE, default=0000)
    transaction_date = models.DateField()

class Salary(models.Model):
    employee_id = models.OneToOneField(
        Employee, on_delete=CASCADE, primary_key=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    basic_salary = models.IntegerField()

class Allowance(models.Model):
    employee_id = models.OneToOneField(
        Employee, on_delete=CASCADE, primary_key=True)

    bonus = models.IntegerField()
    amount_of_allowances = models.IntegerField()

class Attendance(models.Model):
    employee_id = models.OneToOneField(
        Employee, on_delete=CASCADE, primary_key=True)

    working_hours = models.IntegerField()

class Deduction(models.Model):
    employee_id = models.OneToOneField(
        Employee, on_delete=CASCADE, primary_key=True)

    provident_fund = models.IntegerField()
    ammount_of_deduction = models.IntegerField()

class Leave(models.Model):
    employee_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    leave_date = models.DateField(default=datetime.now)
    reason = models.CharField(max_length=30,default='XYZ')


