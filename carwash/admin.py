from django.contrib import admin
from carwash.models import Client, Card, Washer, Administrator, Location, AdministratorLocation


class AdministratorLocationInline(admin.TabularInline):
    model = AdministratorLocation
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_filter = ['discount_card']
    list_display = ['__str__', 'type', 'discount_card']


@admin.register(Card)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['vip']
    list_display = ['vip', 'limit', 'card_administrator']


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'order']
    readonly_fields = ['phone']


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    inlines = [AdministratorLocationInline]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [AdministratorLocationInline]
