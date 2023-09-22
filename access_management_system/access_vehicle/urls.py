from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('vehicle_list/',views.vehicle_list , name= 'vehicle_list'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    
    path('update_vehicle/<int:vehicle_id>/',views.update_vehicle, name='update_vehicle'),
    path('delete_vehicle/<int:vehicle_id>/', views.delete_vehicle , name= 'delete_vehicle'),
    path('admin_list/',views.admin_list, name='admin_list'),
    path('add_admin/',views.add_admin, name='add_admin'),
    path('delete_admin/<int:user_id>/',views.delete_admin , name='delete_admin'),
    path('user_logout/',views.user_logout, name='user_logout'),


]
