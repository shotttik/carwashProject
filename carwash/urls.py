from django.urls import path
from carwash.views import home, contact, blog

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog')
]
