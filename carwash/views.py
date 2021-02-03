from django.shortcuts import render, get_object_or_404
from user.status_choices import Status
from user.models import User
# from carwash.models import Order
from django.db.models import Count


def washer_list(request):
    washers = User.objects.filter(status=Status.washer.value).annotate(washed_count=Count('orders'))
    return render(request, 'pages/washer_list.html', {'washers': washers})


def washer_detail(request, pk: int):
    washer: User = get_object_or_404(
        User.objects.filter(status=Status.washer.value),
        pk=pk
    )
    return render(request, template_name='pages/washer_detail.html', context={'washer': washer})

# def order(request):
#     orders = Order.objects.all()[::-1]
#     orders_count = Order.objects.count()
#     return render(request, 'pages/order.html', {'orders': orders,
#                                                 'orders_count': orders_count})
