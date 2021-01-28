import django_filters
from carwash.models import Order


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ('type', 'plate_number', 'coupons', 'washer')
