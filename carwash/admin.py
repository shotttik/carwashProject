from django.contrib import admin
from carwash.models import VehicleType, Vehicle, Order


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'price']


@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    list_display = ['__str__', 'manufacturer', 'model', 'plate_number']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'washer']
