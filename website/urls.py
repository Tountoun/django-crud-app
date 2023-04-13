from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('add', views.add_employee, name='add_employee'),
    path('detail/<int:pk>', views.employee_detail, name='emp_detail'),
    path('delete/<int:pk>', views.delete_employee, name='delete_emp'),
    path('update/<int:pk>', views.update_employee, name='update_emp')
]
