from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    serial_number = models.IntegerField(unique=True)
    part_number = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class TodayUsage(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    mechanic = models.CharField(max_length=100)
    quantity_used = models.IntegerField()
    model = models.CharField(max_length=100)
    usage_date = models.DateField(auto_now=True)


