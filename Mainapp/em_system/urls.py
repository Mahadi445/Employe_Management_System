from django.contrib import admin
from django.urls import path
from em_system import views as v

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', v.Dashboard_Page, name='Dashboard'), 
    path('profile/', v.Contact_Page, name='Contact_Page'),
]
