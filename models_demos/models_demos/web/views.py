from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from models_demos.web.models import Employee, Department


# Create your views here.
def index(request):
    employees = [e for e in Employee.objects.all() if e.department_id == 3]

    # employees2 = Employee.objects.filter(department_id=2)\
    employees2 = Employee.objects \
        .filter(department__name='Engineering') \
        .filter(age__range=(5, 25)) \
        .order_by('last_name', 'first_name')
    #
    department = Department.objects.get(pk=1)
    #
    # get_object_or_404(Employee, level=Employee.LEVEL_SENIOR)

    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department

    }
    return render(request, 'index.html', context)


def delete_employee(request, pk):
    employee=get_object_or_404(Employee,pk=pk)
    employee.delete()

    return redirect('index')
