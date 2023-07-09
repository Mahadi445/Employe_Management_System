from django.contrib import admin
from django.urls import path
from Employe import views as v

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('emp_list/', v.EmployeList_Page, name='Employe_List'), 
    path('emp_page/', v.EmployeFormSave_page, name='Employe_Form'),
    path('emp_view/<int:id>', v.EmployeDetailsView_page, name='Employe_View_Profile'),  
    path('emp_edit/<int:id>', v.EmployeEdit_Page, name='Employe_Edit'), 
    path('emp_delete/<int:id>', v.EmployeDelete_page, name='Employe_Delete'),
     path('emp_data/', v.EmployeFilterData_page, name='Employe_Filter_Data'),  
]
