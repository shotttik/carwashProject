from django.shortcuts import render
from carwash.models import Coupon, Manager


def home(request):
    coupons = Coupon.objects
    managers = Manager.objects
    return render(request, 'home.html', {'coupons': coupons,
                                         'managers': managers})
