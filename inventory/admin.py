from django.contrib import admin
from .models import InventoryItem, TodayUsage, Brand

admin.site.register(InventoryItem)
admin.site.register(TodayUsage)
admin.site.register(Brand)
