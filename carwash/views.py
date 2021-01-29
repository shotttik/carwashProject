from django.shortcuts import render
from carwash.models import Manager, Washer, Order


def team(request):
    washers = Washer.objects.all
    managers = Manager.objects.all
    return render(request, 'team.html', {'washers': washers,
                                         'managers': managers})


def order(request):
    orders = Order.objects.all()
    order_count = orders.count()
    return render(request, 'order.html', {'orders': orders,
                                          'orders_count': order_count})
