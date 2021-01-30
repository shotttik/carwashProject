from django.urls import path
from carwash.views import base

urlpatterns = [
    path('base/', base, name='base')
]
