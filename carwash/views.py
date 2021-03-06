from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, F, Q, ExpressionWrapper, DecimalField, Sum
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from decimal import Decimal
from typing import Dict, Optional

from user.status_choices import Status
from user.models import User
from carwash.models import Order, VehicleType, WashType, Vehicle
from django.utils import timezone

from carwash.forms import VehicleForm, OrderForm


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
    vehicle_form = VehicleForm()
    order_form = OrderForm()
    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST)
        order_form = OrderForm(request.POST)
        try:
            if vehicle_form.is_valid() and order_form.is_valid():
                vehicle: Vehicle = vehicle_form.save(commit=False)
                vehicle.save()
                order: Order = order_form.save(commit=False)
                order.vehicle = vehicle
                order_date = request.POST.get('order_date')
                completion_date = request.POST.get('completion_date')
                order.order_date = order_date
                order.completion_date = completion_date
                order.washer_id = pk
                order.save()
                return redirect('washer_detail', pk=pk)
        except TypeError:
            vehicle_form.add_error('manufacturer', 'Please Input Correctly! DONT ENTER SYMBOLS!')

    return render(request, template_name='pages/washer_detail.html', context={'washer': washer,
                                                                              **washer_salary_info,
                                                                              'vehicle_types': vehicle_types,
                                                                              'wash_types': wash_types,
                                                                              'vehicle_form': vehicle_form,
                                                                              'order_form': order_form})


def orders(request):
    all_order = Order.objects.all()[::-1]
    orders_count = Order.objects.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_order, 5)
    try:
        allorder = paginator.page(page)
    except PageNotAnInteger:
        allorder = paginator.page(1)
    except EmptyPage:
        allorder = paginator.page(paginator.num_pages)

    return render(request, 'pages/orders.html', {'orders': all_order[::-1],
                                                 'orders_count': orders_count,
                                                 'allorder': allorder})


def homepage(request):
    vehicle_types = VehicleType.objects.all()
    wash_types = WashType.objects.all()
    washers = User.objects.filter(status=Status.washer.value)
    orders_count = Order.objects.all().count()
    return render(request, 'pages/homepage.html', {'vehicle_types': vehicle_types,
                                                   'washers': washers,
                                                   'wash_types': wash_types,
                                                   'orders_count': orders_count})
