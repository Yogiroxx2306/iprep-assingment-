from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from main.models import Company
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Employee
employees = Employee.objects.all()


def companies_view(request):
    companies = Company.objects.all()
    context = {"companies": []}
    # passing python dictionary in context to display the data using proper query
    for company in companies:
        employees = Employee.objects.filter(company=company)
        employee_names = ', '.join([f"{employee.first_name} {employee.last_name}" for employee in employees])
        context["companies"].append({"company": company, "employee_names": employee_names})
    return render(request, 'companies.html', context)

def EmployeeAdd(request):
    # getting company name from url,each url when clicked will have company name embedded into it
    company_name  = request.GET.get('q')
    print(company_name)
    # get company object
    company = get_object_or_404(Company, name=company_name)
    employees = Employee.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = Employee.objects.get(id=employee_id)
        # employee can only be linked to one company,here's a check for that
        if employee.company is not None:
            return render(request, 'error.html', {'message': f'Employee {employee.first_name} {employee.last_name} already belongs to {employee.company.name}'})
        elif employee.company is None:    
            employee.company = company
        employee.save()
        # when done redirect to home page
        return redirect('/')
    context = {
        'companies': company,
        'employees': employees
    }
    return render(request, 'employeelist.html', context)

    


