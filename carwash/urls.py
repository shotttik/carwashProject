from django.urls import path
from carwash.views import washer_list, washer_detail, orders

urlpatterns = [
    path('washers/', washer_list, name='washer_list'),
    path('washers/<int:pk>/', washer_detail, name='washer_detail'),
    path('orders/', orders, name='orders')
]
