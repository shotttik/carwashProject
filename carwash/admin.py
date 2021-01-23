from django.contrib import admin
from carwash.models import ClientModel, CardModel, WasherModel, Administrator, Location, AdministratorLocation


class AdministratorLocationInline(admin.TabularInline):
    model = AdministratorLocation
    extra = 1


@admin.register(ClientModel)
class ClientModel(admin.ModelAdmin):
    list_filter = ['discount_card']
    list_display = ['__str__', 'type', 'discount_card']


@admin.register(CardModel)
class StatusModel(admin.ModelAdmin):
    search_fields = ['vip']
    list_display = ['vip', 'limit']


@admin.register(WasherModel)
class WasherModel(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'order' ]
    readonly_fields = ['phone']


@admin.register(Administrator)
class AdministratorModel(admin.ModelAdmin):
    inlines = [AdministratorLocationInline]
    readonly_fields = ['personal_number']


@admin.register(Location)
class LocationModel(admin.ModelAdmin):
    inlines = [AdministratorLocationInline]
