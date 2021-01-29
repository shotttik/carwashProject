from django.contrib import admin
from carwash.models import VehicleType, Vehicle, Washer, Order, Manager


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'joined', 'show_order_percent']


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'show_price']


@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    list_display = ['plate_number', 'get_type', 'get_price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'type', 'price', 'order_date', 'completion_date', 'washer', 'earned']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'email', 'phone']
