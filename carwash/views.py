from django.shortcuts import render, get_object_or_404
from user.status_choices import Status
from user.models import User
from carwash.models import Order
from django.db.models import Count, F, Q, ExpressionWrapper, DecimalField, Sum
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from decimal import Decimal
from typing import Dict, Optional


def washer_list(request: WSGIRequest) -> HttpResponse:
    washer_q = Q()
    order_q = Q()
    q = request.GET.get('q')

    if q:
        washer_q &= Q(first_name__icontains=q[-1]) | Q(last_name__icontains=q[-1])
        order_q &= Q(washer__first_name__icontains=q[-1]) | Q(employee__last_name__icontains=q[-1])

    profit_q = ExpressionWrapper(
        F('price') * (1 - F('washer__salary') / Decimal('100.0')),
        output_field=DecimalField()
    )
    order_info: Dict[str, Optional[Decimal]] = Order.objects.filter(completion_date__isnull=False).filter(order_q)\
        .annotate(profit_per_order=profit_q)\
        .aggregate(profit=Sum('profit_per_order'), total=Count('id'))

    context = {
        'washers': User.objects.filter(status=Status.washer.value).filter(washer_q).annotate(
            washed_count=Count('orders')),

    }
    context.update(order_info)
    return render(request, 'pages/washer_list.html', context=context)


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
