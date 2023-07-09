from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EmployeesForm
from .models import Employees
from Department.models import Department
from Position.models import Position
from django.db.models import Q
# Create your views here.



def EmployeList_Page(request):
    emp = Employees.objects.all()
    return render (request,'employe/employelist.html',{'Employe':emp})


def EmployeFormSave_page(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['code']
            fn = form.cleaned_data['firstname']
            ln = form.cleaned_data['lastname']
            dob = form.cleaned_data['dob']
            gn = form.cleaned_data['gender']
            dh = form.cleaned_data['date_hired'] 
            d_id = form.cleaned_data['department_id'] 
            p_id = form.cleaned_data['position_id']
            sa = int(form.cleaned_data['salary'])
            su = form.cleaned_data['status']
            em = form.cleaned_data['email']
            co = form.cleaned_data['contact']
            ad = form.cleaned_data['address']
            
            data =Employees(code=cd,firstname=fn,lastname=ln,gender=gn,dob=dob,contact=co,address=ad,email=em,department_id=d_id,position_id=p_id,date_hired=dh,salary=sa,status=su,)
            data.save()
            return redirect('Employe_List')  
        else:
            print(form.errors)
    else:
        form = EmployeesForm()
    departments = Department.objects.all()
    positions = Position.objects.all()
    context = {
        'form': form,
        'departments': departments,
        'positions': positions
    }
    return render(request, 'employe/employeform.html', context)


def EmployeDetailsView_page(request,id):
    data= Employees.objects.get(id = id)
    context={
        'view' : data
    }
    return render (request,'employe/employeview.html',context)


def EmployeDelete_page(request, id):
    emp_delete = get_object_or_404(Employees, id=id)
    if request.method == 'POST':
        emp_delete.delete()
    return render (request,'employe/employedelete.html',{'emps_delete':emp_delete})


def EmployeEdit_Page(request, id):
    employe = get_object_or_404(Employees, id=id)
    if request.method == 'POST':
        form = EmployeesForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()  
            return redirect('Employe_List')
        else:
            print(form.errors)
    else:
        form = EmployeesForm(instance=employe)
    departments = Department.objects.all()
    positions = Position.objects.all()
    context = {
        'form': form,
        'emps': employe,
        'departments': departments,
        'positions': positions
    }
    return render(request, 'employe/employedit.html', context)



def EmployeFilterData_page(request):
        dep = Department.objects.select_related('department_id').values('id', 'depart_name').distinct()
        pos = Position.objects.select_related('position_id').values('id', 'position_name').distinct()    
        context = {
            'data1' : dep,
            'data2' : pos
        }
        return render(request, 'employe/employefilter.html', context)
    
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 




    # if request.method == 'POST':
    #     # name = request.POST.get('name')
    #     depart = request.POST.get('Department')
    #     position = request.POST.get('Position')
    #     employees = Employees.objects.all()
        
    #     # if name:
    #     #     employees = employees.filter(Q(firstname__icontains=name) | Q(lastname__icontains=name))

    #     if depart:
    #         employees = employees.filter(Q(department_id__depart_name__icontains=depart))

    #     if position:
    #         employees = employees.filter(Q(position_id__position_name__icontains=position))

    #     context = {
    #         'Employee': employees,  # Renamed the key to 'Employee' for consistency
    #     }
    #     return render(request, 'employe/employefilterlist.html', context)
    # else:
        # return render(request, 'employe/employefilter.html')










