from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('submit/', views.submit_vehicle, name='submit_vehicle'),
    path('vehicles/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('vehicles/<int:vehicle_id>/inquiry/',views.vehicle_inquiry,name='vehicle_inquiry'),
    path('delete/<int:vehicle_id>/',views.delete_vehicle,name="delete_vehicle")
]
