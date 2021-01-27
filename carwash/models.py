from django.db import models
from django.contrib.auth.models import User
from carwash.vehichle_type_choices import VehicleTypeChoices
from carwash.vip_status_choices import VipStatusChoices

''' 
    კუპონების გამოყენება ხდება ერჯერადად, არის რამდენიმე სტატუსის მქონე, ერთი სტატუსის შეიძლება ბევრი იყოს გამოშვებული.
    ავტომობილს შეუძლია ერთი სახეობის კუპონით გარეცხვა ბევრჯერ.
'''


class Coupon(models.Model):
    vip_status = models.CharField(max_length=255, choices=VipStatusChoices.choices,
                                  default=VipStatusChoices.Bronze,
                                  unique=True)  # ერთი სტატუსის ორი კუპონი რომ არ შეიქმნას
    discount = models.CharField(max_length=255, verbose_name='Discount')
    gift = models.TextField(verbose_name='Gift', blank=True)

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
    # coupons = models.ManyToManyField(to='carwash.Coupon', blank=True) ერთ გარეცხვაზე რამდენიმე კუპონის გამოყენება არშე
    coupons = models.ForeignKey(to='carwash.Coupon',
                                on_delete=models.PROTECT,  # კუპონი არ წაიშლება შეიცვლება ფასდაკლება ან საჩუქარი.
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
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)  # user თუ წაიშლება მენეჯერიც რომ წაიშალოს
    full_name = models.CharField(verbose_name='Full Name', max_length=255, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', default=0)
    email = models.EmailField(verbose_name="E-mail", unique=True)
    phone = models.CharField(verbose_name='Mobile phone number', max_length=9, unique=True)
    personal_number = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name
