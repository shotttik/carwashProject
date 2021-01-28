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
    gift = models.CharField(max_length=255, verbose_name='Gift', blank=True)

    def __str__(self):
        return self.vip_status

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'


class Order(models.Model):
    type = models.PositiveSmallIntegerField("Vehicle Type", choices=VehicleTypeChoices.choices,
                                            default=VehicleTypeChoices.Sedan)
    plate_number = models.CharField(max_length=15, unique=False)  # ერთი ავტომობილი ბევრჯერ გაირეცხოს
    started = models.DateTimeField(verbose_name='Started')
    finished = models.DateTimeField(verbose_name='Finished', auto_now=True)  # გარეცხვის შემდეგ შედის ბაზაში
    coupons = models.ForeignKey(to='carwash.Coupon',
                                on_delete=models.PROTECT,  # კუპონი არ წაიშლება შეიცვლება ფასდაკლება ან საჩუქარი.
                                blank=True, null=True)  # კუპონის გარეშე მანქანის გარეცხვა
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    washer = models.ForeignKey(to='carwash.Washer',
                               on_delete=models.SET_NULL,  # მრეცხავის წაშლის შემთხვევაში გარეცხილი მანქანა რომ დარჩეს
                               null=True)

    def __str__(self):
        return f'{self.plate_number} - {self.price}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Washer(models.Model):
    full_name = models.CharField(verbose_name='Full name', max_length=255, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', default=0)
    phone = models.CharField(verbose_name='Mobile phone number', max_length=9, unique=True)
    joined = models.DateTimeField(verbose_name="Joined", auto_now=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Washer'
        verbose_name_plural = 'Washers'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    manager = models.ForeignKey(to='carwash.Manager',
                                on_delete=models.SET_NULL, null=True)  # მენეჯერის წაშლის შემთხვევაში პოსტი რომ დარჩეს

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


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

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'
