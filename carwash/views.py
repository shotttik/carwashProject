from django.shortcuts import render
from user.status_choices import Status
from user.models import User
from carwash.models import Order
from django.db.models import Count


def base(request):
    washers = User.objects.filter(status=Status.washer.value).annotate(washed_count=Count('orders'))
    return render(request, 'pages/team.html', {'washers': washers})


def order(request):
    orders = Order.objects.all()[::-1]
    orders_count = Order.objects.count()
    return render(request, 'pages/order.html', {'orders': orders,
                                                'orders_count': orders_count})
