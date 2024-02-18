from django import forms
from .models import InventoryItem, TodayUsage

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['serial_number', 'part_number', 'description', "brand", "quantity", "price"]

class UsageForm(forms.ModelForm):
    class Meta:
        model = TodayUsage
        fields = ["mechanic", "quantity_used", "model"]
