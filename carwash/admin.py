from django.contrib import admin
from carwash.models import WashedVehicle, Coupon, Washer, Manager


@admin.register(WashedVehicle)
class WashedVehicleAdmin(admin.ModelAdmin):
    list_filter = ['coupons', 'type']
    list_display = ['type', 'plate_number', 'started', 'finished', 'washer']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['vip_status', 'gift', ]


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'joined', 'manager']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'age', 'phone']
