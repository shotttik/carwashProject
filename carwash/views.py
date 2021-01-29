from django.shortcuts import render
from carwash.models import Manager, Washer, Order


def team(request):
    customer = Washer.objects.get()
    washer_orders = customer.orders.all()
    orders_count = washer_orders.count()
    washers = Washer.objects.all
    managers = Manager.objects.all
    return render(request, 'team.html', {'washers': washers,
                                         'managers': managers,
                                         'orders_count': orders_count,
                                         })


def order(request):
    orders = Order.objects.all().order_by('-id')
    order_count = orders.count()
    return render(request, 'order.html', {'orders': orders,
                                          'orders_count': order_count})
