import django_filters
from carwash.models import Order
from django_filters import DateFilter


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_ordered", lookup_expr='gte', label='Date greater than')
    end_date = DateFilter(field_name='date_ordered', lookup_expr='lte', label='Date less than')

    class Meta:
        model = Order
        fields = ('type', 'plate_number', 'coupons', 'washer')
