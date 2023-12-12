from django.contrib import admin
from django.urls import path
from employee.views import homeview
from employee.views import empformview
from employee.views import detailsview
from django.contrib import admin  
from django.urls import path  
from employee import views  



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',homeview),
    path('empform',empformview),
    path('detailsview',detailsview)
]

#crud url

path('emp',emp),
path('show',show),
path('edit/<int:id>',edit),
path('update',update),