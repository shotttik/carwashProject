from django.contrib import admin
from carwash.models import Coupon, Washer, Manager, Order


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['vip_status', 'discount', 'gift', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['type', 'plate_number', 'price', 'washer', 'earned']
    list_filter = ['type', 'washer', 'plate_number']


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'joined']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'age', 'phone', 'email']


# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title', 'pub_date', 'manager']
