from django.shortcuts import render
from user.status_choices import Status
from user.models import User
from django.db.models import Count


def base(request):
    washers = User.objects.filter(status=Status.washer.value).annotate(washed_count=Count('orders'))
    return render(request, 'pages/team.html', {'washers': washers})


def orders(request):
    return render(request, 'pages/order.html')
