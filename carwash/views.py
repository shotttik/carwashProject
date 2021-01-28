from django.shortcuts import render
from carwash.models import Coupon, Manager, Washer, Blog


def home(request):
    coupons = Coupon.objects.all
    washers = Washer.objects.all
    return render(request, 'home.html', {'coupons': coupons,
                                         'washers': washers})


def about(request):
    managers = Manager.objects.all
    return render(request, 'about.html', {'managers': managers})


def blog(request):
    blogs = Blog.objects.all
    return render(request, 'blog.html', {'blogs': blogs})
