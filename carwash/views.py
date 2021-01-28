from django.shortcuts import render
from carwash.models import Coupon, Manager, Washer, Blog, Order


def home(request):
    coupons = Coupon.objects.all
    washers = Washer.objects.all
    return render(request, 'home.html', {'coupons': coupons,
                                         'washers': washers})


def contact(request):
    managers = Manager.objects.all
    return render(request, 'contact.html', {'managers': managers})


def blog(request):
    blogs = Blog.objects.all
    return render(request, 'blog.html', {'blogs': blogs})


def services(request):
    orders = Order.objects.all
    return render(request, 'services.html', {'orders': orders})
