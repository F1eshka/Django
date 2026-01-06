from django.contrib import admin
from django.urls import path
from tasks.views import current_datetime, multiplication_table, programmer_day

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datetime/', current_datetime, name='datetime'),  
    path('table/', multiplication_table, name='table'),    
    path('programmer/', programmer_day, name='programmer'),
]