from django.contrib import admin
from django.urls import path
from Position import views as v

urlpatterns = [
    path('pos_page/', v.Position_Page, name='Position_Add'),
    path('pos_list/', v.Positionlist_page, name='Position_List'), 
    path('pos_edit/<int:id>', v.PositionEdit_Page, name='Position_Edit'), 
    path('pos_delete/<int:id>', v.PositionDelete_Page, name='Position_Delete'), 
]
