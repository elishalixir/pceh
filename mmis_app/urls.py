from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
    path('health/', views.health, name='health'),
    path('cement/', views.cement_sector, name='cement'),
    #Create - MAP
    path('map_create/', views.map_create, name='map_create'),
    #Read - MAP
    path('map_read/', views.map_read, name='map_read'),
    # Update - MAP
    path('map_edit/<int:map_id>', views.map_edit, name='map_edit'),
    #Update - MAP
    path('map_update/<int:map_id>', views.map_update, name='map_update'),
    #Delete - MAP
    path('map_delete/<int:map_id>', views.map_delete, name='map_delete'),

# Energy consumption and fuel production
    path('energy/', views.energy_fuel, name='energy'),
    # Create - energyfuel
    path('ecfp_create/', views.ecfp_create, name='ecfp_create'),
    # Read - energyfuel
    path('ecfp_read/', views.ecfp_read, name='ecfp_read'),
    # Update - energyfuel
    path('ecfp_edit/<int:ecfp_id>', views.ecfp_edit, name='ecfp_edit'),
    # Update - energyfuel
    path('ecfp_update/<int:ecfp_id>', views.ecfp_update, name='ecfp_update'),
    # Delete - energyfuel
    path('ecfp_delete/<int:ecfp_id>', views.ecfp_delete, name='ecfp_delete'),
    path('Asgm/', views.Asgm, name='Asgm'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login_view'),

]
