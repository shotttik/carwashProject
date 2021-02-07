from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, F, Q, ExpressionWrapper, DecimalField, Sum
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from decimal import Decimal
from typing import Dict, Optional

from user.status_choices import Status
from user.models import User
from carwash.models import Order, VehicleType, WashType
from django.utils import timezone


def washer_list(request: WSGIRequest) -> HttpResponse:
    washer_q = Q()
    order_q = Q()
    q = request.GET.get('q')

    if q:
        washer_q &= Q(first_name__icontains=q) | Q(last_name__icontains=q)
        order_q &= Q(washer__first_name__icontains=q[-1]) | Q(washer__last_name__icontains=q[-1])

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


def washer_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    now = timezone.now()
    washer: User = get_object_or_404(
        User.objects.filter(status=Status.washer.value),
        pk=pk
    )
    earned_money_q = ExpressionWrapper(
        F('price') * F('washer__salary') / Decimal('100.0'),
        output_field=DecimalField()
    )
    washer_salary_info: Dict[str, Optional[Decimal]] = washer.orders.filter(completion_date__isnull=False)\
        .annotate(earned_per_order=earned_money_q)\
        .aggregate(
        earned_money_year=Sum(
            'earned_per_order',
            filter=Q(completion_date__gte=now - timezone.timedelta(days=365))
        ),
        washed_last_year=Count(
            'id',
            filter=Q(completion_date__gte=now - timezone.timedelta(days=365))
        ),
        earned_money_month=Sum(
            'earned_per_order',
            filter=Q(completion_date__gte=now - timezone.timedelta(weeks=4))
        ),
        washed_last_month=Count(
            'id',
            filter=Q(completion_date__gte=now - timezone.timedelta(weeks=4))
        ),
        earned_money_week=Sum(
            'earned_per_order',
            filter=Q(completion_date__gte=now - timezone.timedelta(days=7))
        ),
        washed_last_week=Count(
            'id',
            filter=Q(completion_date__gte=now - timezone.timedelta(days=7))
        )
    )
    vehicle_types = VehicleType.objects.all()
    wash_types = WashType.objects.all()
    if request.method == 'POST':
        manufacturer = request.POST.get('manufacturer')
        model = request.POST.get('model')
        plate_number = request.POST.get('plate_number')
        vehicle_type = request.POST.get('vehicle_type')
        wash_type = request.POST.get('wash_type')
        print(manufacturer, model, plate_number, vehicle_type, wash_type)
        order = Order(order_date=timezone.now(), wash_type_id=wash_type, washer_id=pk)
        order.save()
        return redirect('washer_detail', pk=pk)

    return render(request, template_name='pages/washer_detail.html', context={'washer': washer,
                                                                              **washer_salary_info,
                                                                              'vehicle_types': vehicle_types,
                                                                              'wash_types': wash_types})

# def order(request):
#     orders = Order.objects.all()[::-1]
#     orders_count = Order.objects.count()
#     return render(request, 'pages/order.html', {'orders': orders,
#                                                 'orders_count': orders_count})
