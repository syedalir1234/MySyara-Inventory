from datetime import datetime, date
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem, TodayUsage
from .forms import InventoryItemForm, UsageForm

def inventory_list(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'inventory_list.html', {'inventory_items': inventory_items})

def add_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        serial_number = datetime.now().strftime('%Y%m%d%H%M%S')
        form.instance.serial_number = serial_number

        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'add_inventory_item.html', {'form': form})

def edit_inventory_item(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm(instance=inventory_item)
    return render(request, 'edit_inventory_item.html', {'form': form})

def delete_inventory_item(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        inventory_item.delete()
        return redirect('inventory_list')
    return render(request, 'delete_inventory_item.html', {'inventory_item': inventory_item})

def record_usage(request, inventory_item_id):
    inventory_item = InventoryItem.objects.get(pk=inventory_item_id)
    if request.method == 'POST':
        form = UsageForm(request.POST)
        form.instance.inventory_item = inventory_item
        if form.is_valid():
            form.save()
            return redirect('usage_list')
        else:
            print(form.errors)
    else:
        form = UsageForm(initial={
            'inventory_item': inventory_item
        })
    return render(request, 'record_usage.html', {'form': form})

def usage_list(request):
    # today_usages = TodayUsage.objects.all()
    today = date.today()
    today_usages = TodayUsage.objects.filter(
        Q(usage_date__year=today.year) &
        Q(usage_date__month=today.month) &
        Q(usage_date__day=today.day)
    )
    return render(request, 'usage_list.html', {'today_usages': today_usages})

def all_usage_list(request):
    all_usages = TodayUsage.objects.all()
    return render(request, 'usage_list.html', {'today_usages': all_usages})
