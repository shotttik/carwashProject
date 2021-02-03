from django.urls import path
from carwash.views import washer_list, washer_detail

urlpatterns = [
    path('washers/', washer_list, name='washer_list'),
    path('washers/<int:pk>/', washer_detail, name='washer_detail')
]
