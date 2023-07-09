from django.shortcuts import render
from Department.models import Department
from Position.models import Position
from Employe.models import Employees
# Create your views here.


def Dashboard_Page(request):
    
    CountOne = len(Department.objects.all())
    CountTwo = len(Position.objects.all())
    CountTree = len(Employees.objects.all())
    context={
        'CountOne': CountOne,
        'CountTwo' : CountTwo,
        'CountTree' : CountTree,
    }
    return render (request, 'ems_temp/Dashboard_page.html',context)

def Contact_Page(request):
    return render (request, 'ems_temp/contact.html')

