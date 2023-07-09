from django.contrib import admin
from django.urls import path
from Department import views as v
urlpatterns = [
    path('depart_page/', v.Department_page, name='Department_Add'),
    path('depart/', v.Departmentlist_page, name='Department_List'), 
    path('depart_edit/<int:id>', v.DepartmentEdit_Page, name='Department_Edit'), 
    path('depart_delete/<int:id>', v.DepartmentDelete_Page, name='Department_Delete'), 
]