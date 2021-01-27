from django.urls import path
from carwash.views import home

urlpatterns = [
    path('', home, name='home'),
]
