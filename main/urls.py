from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('addemployee/', views.EmployeeAdd,name='EmployeeAdd'),
]

# addemployee/companyname is the url,where i will get company name using params
