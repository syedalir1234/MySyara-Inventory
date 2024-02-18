
from django.contrib import admin
from django.urls import path
from inventory import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inventory_list, name='inventory_list'),  # Home page
    path('add/', views.add_inventory_item, name='add_inventory_item'),
    path('inventory_list/', views.inventory_list, name='inventory_list'),  # Inventory list view
    path('usage/<int:inventory_item_id>', views.record_usage, name='record_usage'),
    path('usage_list/', views.usage_list, name='usage_list'),
    path('edit/<int:pk>/', views.edit_inventory_item, name='edit_inventory_item'),
    path('delete_inventory_item/<int:pk>/', views.delete_inventory_item, name='delete_inventory_item'),
    path('all_usage_list/', views.all_usage_list, name='all_usage_list'),
]
