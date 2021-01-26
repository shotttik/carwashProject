from django.db import models
from carwash.vehichle_type_choices import VehicleTypeChoices
from carwash.vip_status_choices import VipStatusChoices


# იდეაში ერთჯერადი კუპონებია.
class Coupon(models.Model):
    vip_status = models.CharField(max_length=255, choices=VipStatusChoices.choices,
                                  default=VipStatusChoices.Bronze)
    discount = models.CharField(max_length=255, verbose_name='Discount')
    gift = models.TextField(verbose_name='Gift', blank=True)  # კუპონი არ წაიშლება შეიცვლება ფასდაკლება ან საჩუქარი.

    def __str__(self):
        return self.vip_status

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'


class Vehicle(models.Model):
    type = models.PositiveSmallIntegerField("Vehicle Type", choices=VehicleTypeChoices.choices,
                                            default=VehicleTypeChoices.Sedan)
    started = models.DateTimeField(verbose_name='Started')
    finished = models.DateTimeField(verbose_name='Finished', auto_now=True)  # გარეცხვის შემდეგ შედის ბაზაში
    plate_number = models.CharField(max_length=15)  # unique=False რათა ბევრჯერ გაირეცხოს
    coupons = models.ForeignKey(to='carwash.Coupon', on_delete=models.PROTECT,
                                blank=True, null=True)  # კუპონის გარეშე მანქანის გარეცხვა
    washer = models.ForeignKey(to='carwash.Washer',
                               on_delete=models.SET_NULL,  # მრეცხავის წაშლის შემთხვევაში გარეცხილი მანქანა რომ დარჩეს
                               null=True)

    def __str__(self):
        return self.plate_number

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Washer(models.Model):
    full_name = models.CharField(verbose_name='Full name', max_length=255, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', default=0)
    phone = models.CharField(verbose_name='Mobile phone number', max_length=9, unique=True)
    joined = models.DateTimeField(verbose_name="Joined", auto_now=True)
    manager = models.ForeignKey(to='carwash.Manager',
                                   on_delete=models.SET_NULL,  # მენეჯერის წაშლის შემთხვევაში მრეცხავი რომ ბაზაში დარჩეს
                                   null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Washer'
        verbose_name_plural = 'Washers'


class Manager(models.Model):
    full_name = models.CharField(verbose_name='Full Name', max_length=255, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', default=0)
    email = models.EmailField(verbose_name="E-mail", unique=True)
    phone = models.CharField(verbose_name='Mobile phone number', max_length=9, unique=True)
    personal_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.full_name
