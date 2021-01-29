# from django.shortcuts import render
# from carwash.models import Coupon, Manager, Washer, Order
# from carwash.filters import OrderFilter
#
#
# def team(request):
#     coupons = Coupon.objects.all
#     washers = Washer.objects.all
#     managers = Manager.objects.all
#     return render(request, 'team.html', {'coupons': coupons,
#                                          'washers': washers,
#                                          'managers': managers})
#
#
# def order(request):
#     orders = Order.objects.all()
#     order_count = orders.count()
#     order_filter = OrderFilter(request.GET, queryset=orders)
#     orders = order_filter.qs
#     return render(request, 'order.html', {'orders': orders,
#                                              'orders_count': order_count,
#                                              'order_filter': order_filter})
