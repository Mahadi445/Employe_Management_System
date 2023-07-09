from django.shortcuts import render, redirect, get_object_or_404
from Department.models import Department
from Department.forms import DepartmentForm



def Department_page(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Department_List')
    else:
        form = DepartmentForm()
    return render(request, 'Depart/Department_page.html', {'form': form})



def DepartmentEdit_Page(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('Department_List')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'Depart/DepartmentEdit_page.html', {'form': form, 'department': department})

def DepartmentDelete_Page(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('Department_List')
    return render(request, 'Depart/DepartmentDelete.html', {'department': department})

def Departmentlist_page(request):
    departments = Department.objects.all()
    return render(request, 'Depart/Departmentlist_page.html', {'departments': departments})



























# from django.shortcuts import redirect, render,get_object_or_404
# from Department.models import Department
# # Create your views here.


# def Department_page(request):
    
#     if request.method == 'POST':
#         Name = request.POST['D_Name']
#         Description = request.POST['D_Description']
#         Status = request.POST.get('D_status', False) == 'True'  
#         Data = Department(depart_name=Name,description=Description,status=Status)
#         Data.save()
        
#     return render (request, 'Depart/Department_page.html')



# def Departmentlist_page(request):
#     Data_list = Department.objects.all()
#     context = {
#         'Data':  Data_list
#     }
#     return render (request, 'Depart/Departmentlist_page.html',context)


# def DepartmentEdit_Page(request, pk):
#     # fetch the object related to passed id
#     obj = get_object_or_404(Department, id = pk)
    
#     if request.method == 'POST':
#         Name = request.POST['D_Name']
#         Description = request.POST['D_Description']
#         Status = request.POST.get('D_status', False) == 'True'  
#         Data = Department(depart_name=Name,description=Description,status=Status)
#         Data.save()
#         return redirect('Department')
    
#     context = {
#         'pk': obj
#     }
#     return render(request, 'Depart/Department_page.html',context)

# def DepartmentDelete_Page(request):
    
#     return render (request,'Depart/DepartmentDelete.html')