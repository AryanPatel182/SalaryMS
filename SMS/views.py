from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Account_detail, Administrator, Allowance, Deduction, Department, Employee, Employee_address, Leave,Login, Phone_number, Salary, Transaction, Attendance
from django.shortcuts import render
import operator



# Create your views here
# .

login_details = {'ABC2019001': '1234', 'ABC2019002': '1234'}

def home_page(request):
    return render(request, 'sms/home.html')

def index_page(request):    
    return render(request, 'sms/index.html')    

def query(request):
    employee_id = 'ABC2019001'
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')

    st = ''' select "SMS_employee".employee_id, street, city, state
    from "SMS_employee","SMS_employee_address"
    where "SMS_employee".employee_id = "SMS_employee_address".employee_id_id and "SMS_employee".employee_id = ''' + "'" + str(employee_id) + "'"
    print(st)
    #     qry = Employee.objects.raw(''' select "SMS_employee".employee_id, first_name, last_name, basic_salary, amount_of_allowances, ammount_of_deduction, net_salary
    # from "SMS_employee","SMS_transaction","SMS_salary","SMS_allowance","SMS_deduction"
    # where "SMS_employee".employee_id = "SMS_transaction".employee_id_id and "SMS_employee".employee_id = "SMS_salary".employee_id_id and
    # "SMS_employee".employee_id = "SMS_allowance".employee_id_id and "SMS_employee".employee_id = "SMS_deduction".employee_id_id  ''' )

    qry = Employee.objects.raw(st)
    return render(request, 'sms/query.html', {'data': qry})

def employee_slip(request):
    employee_id = 'ABC2019001'
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
    # tmp = ''' employee_id '''
    st = ''' select "SMS_employee".employee_id, first_name, last_name, basic_salary, amount_of_allowances, ammount_of_deduction, net_salary 
    from "SMS_employee","SMS_transaction","SMS_salary","SMS_allowance","SMS_deduction"
    where "SMS_employee".employee_id = "SMS_transaction".employee_id_id and "SMS_employee".employee_id = "SMS_salary".employee_id_id and 
    "SMS_employee".employee_id = "SMS_allowance".employee_id_id and "SMS_employee".employee_id = "SMS_deduction".employee_id_id and "SMS_employee".employee_id = ''' + "'" + str(employee_id) + "'"
    print(st)
    #     qry = Employee.objects.raw(''' select "SMS_employee".employee_id, first_name, last_name, basic_salary, amount_of_allowances, ammount_of_deduction, net_salary 
    # from "SMS_employee","SMS_transaction","SMS_salary","SMS_allowance","SMS_deduction"
    # where "SMS_employee".employee_id = "SMS_transaction".employee_id_id and "SMS_employee".employee_id = "SMS_salary".employee_id_id and 
    # "SMS_employee".employee_id = "SMS_allowance".employee_id_id and "SMS_employee".employee_id = "SMS_deduction".employee_id_id  ''' )

    qry = Employee.objects.raw(st)
    return render(request, 'sms/slip.html', {'data': qry})

def leave_slip(request):
    employee_id = 'ABC2019001'
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
    # tmp = ''' employee_id '''
    st = ''' select "SMS_employee".employee_id, "SMS_employee".first_name, count(leave_date) from "SMS_employee" left join "SMS_leave" on "SMS_employee".employee_id = "SMS_leave".employee_id_id where "SMS_employee".employee_id =''' + "'" + str(
        employee_id) + "'" + ''' group by "SMS_employee".employee_id order by "SMS_employee".employee_id '''
    print(st)
    #     qry = Employee.objects.raw(''' select "SMS_employee".employee_id, first_name, last_name, basic_salary, amount_of_allowances, ammount_of_deduction, net_salary 
    # from "SMS_employee","SMS_transaction","SMS_salary","SMS_allowance","SMS_deduction"
    # where "SMS_employee".employee_id = "SMS_transaction".employee_id_id and "SMS_employee".employee_id = "SMS_salary".employee_id_id and 
    # "SMS_employee".employee_id = "SMS_allowance".employee_id_id and "SMS_employee".employee_id = "SMS_deduction".employee_id_id  ''' )

    qry = Employee.objects.raw(st)
    return render(request, 'sms/leave_slip.html', {'data': qry})
    
    

def department_list_items(request):
    context = {'dep_list': Department.objects.all().order_by('department_id')}    
    return render(request, 'sms/department.html', context)    

def employee_list_items(request):
    context = {'emp_list': Employee.objects.all().order_by('employee_id')}
    return render(request, 'sms/employee.html', context)

def employee_address_list_items(request):
    context = {'emp_address_list': Employee_address.objects.all()}
    return render(request, 'sms/employee_address.html', context)

def phone_number_list_items(request):
    context = {'phone_number_list': Phone_number.objects.all()}
    return render(request, 'sms/phone_number.html', context)

def administrator_list_items(request):
    context = {'administrator_list': Administrator.objects.all()}
    return render(request, 'sms/administrator.html', context)

def account_detail_list_items(request):
    context = {'account_detail_list': Account_detail.objects.all()}
    return render(request, 'sms/account_detail.html', context)

def login_list_items(request):
    context = {'login_list': Login.objects.all()}
    return render(request, 'sms/login.html', context)

def transaction_list_items(request):
    context = {'transaction_list': Transaction.objects.all()}
    return render(request, 'sms/transaction.html', context)

def salary_list_items(request):
    context = {'salary_list': Salary.objects.all()}
    return render(request, 'sms/salary.html', context)

def allowance_list_items(request):
    context = {'allowance_list': Allowance.objects.all()}
    return render(request, 'sms/allowance.html', context)

def attendance_list_items(request):
    context = {'attendance_list': Attendance.objects.all()}
    return render(request, 'sms/attendance.html', context)

def deduction_list_items(request):
    context = {'deduction_list': Deduction.objects.all()}
    return render(request, 'sms/deduction.html', context)

def leave_list_items(request):
    context = {'leave_list': Leave.objects.all()}
    return render(request, 'sms/leave.html', context)

def insert_department_item(request):

    if request.method == 'POST':
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department_name')
        department_manager = request.POST.get('department_manager')
        salary_range = request.POST.get('salary_range')

        dep = Department(department_id=department_id, department_name=department_name, department_manager=department_manager, salary_range=salary_range)
        print(dep)
        dep.save()
    return redirect('/department')    


def insert_employee_item(request):

    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        joining_date = request.POST.get('joining_date')
        department_id = request.POST.get('department_id')

        dep = Department(department_id=department_id)
        emp = Employee(employee_id=employee_id, first_name=first_name, last_name=last_name, email=email, gender=gender, dob=dob, joining_date=joining_date, department_id=dep)
        print(emp)
        emp.save()
    return redirect('/employee')


def delete_department_item(request, department_id):
    print(department_id)
    dep_to_delete = Department.objects.get(department_id=department_id)
    dep_to_delete.delete()
    return redirect('/department')


def delete_employee_item(request, employee_id):    
    emp_to_delete = Employee.objects.get(employee_id = employee_id)
    emp_to_delete.delete()
    return redirect('/employee')

