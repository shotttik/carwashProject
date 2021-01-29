from django.urls import path
from carwash.views import team, order

urlpatterns = [
    path('', team, name='team'),
    path('order/', order, name='order')
]
