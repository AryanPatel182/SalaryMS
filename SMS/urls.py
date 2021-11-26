from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('index',views.index_page),
    path('department', views.department_list_items),
    path('employee', views.employee_list_items),
    path('employee_address', views.employee_address_list_items),
    path('phone_number', views.phone_number_list_items),
    path('administrator',views.administrator_list_items),
    path('account_detail', views.account_detail_list_items),
    path('login', views.login_list_items),
    path('transaction', views.transaction_list_items),
    path('salary', views.salary_list_items),
    path('allowance', views.allowance_list_items),
    path('attendance', views.attendance_list_items),
    path('deduction', views.deduction_list_items),
    path('leave', views.leave_list_items),
    path('insert_department', views.insert_department_item),
    path('insert_employee', views.insert_employee_item),
    path('delete_department/<str:department_id>',
         views.delete_department_item),
    path('delete_employee/<str:employee_id>',
         views.delete_employee_item),     
    path('slip', views.employee_slip),    
    path('leave_slip', views.leave_slip),
    path('query', views.query),
]

