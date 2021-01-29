from django.db import models
from django.contrib.auth.models import User
from carwash.vehichle_type_choices import VehicleTypeChoices
# from carwash.vip_status_choices import VipStatusChoices


class VehicleType(models.Model):
    type = models.CharField(max_length=255, verbose_name="Vehicle Type", choices=VehicleTypeChoices.choices,
                            default=VehicleTypeChoices.SEDAN, unique=True)
    price = models.PositiveIntegerField(verbose_name="Price", default=0)

    def __str__(self):
        return f'{self.type} - {self.price}$'

    def show_price(self):
        return self.price


class Washer(models.Model):
    full_name = models.CharField(verbose_name='Full name', max_length=255, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', default=0)
    phone = models.CharField(verbose_name='Mobile phone number', max_length=9, unique=True)
    order_percent = models.PositiveIntegerField(verbose_name='Order percent', default=0)
    joined = models.DateTimeField(verbose_name="Joined", auto_now=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

    def show_order_percent(self):
        return f'{self.order_percent}%'

    class Meta:
        verbose_name = 'Washer'
        verbose_name_plural = 'Washers'


class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=255, verbose_name="Manufacturer")
    model = models.CharField(max_length=255, verbose_name='Model')
    plate_number = models.CharField(max_length=15, verbose_name='Plate Number')
    vehicle_type = models.ForeignKey(to='carwash.VehicleType', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.plate_number} - {self.vehicle_type}"

    def get_type(self):
        return self.vehicle_type.type

    def get_price(self):
        return self.vehicle_type.price

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Order(models.Model):
    order_date = models.DateTimeField("Order date")
    completion_date = models.DateTimeField("Completion date")
    vehicle = models.ForeignKey(to="carwash.Vehicle", on_delete=models.CASCADE, related_name='orders')
    washer = models.ForeignKey(to='carwash.Washer', related_name='orders',
                               on_delete=models.SET_NULL, null=True)  # მრეცხავის წაშლის შემთხვევაში ორდერი რომ დარჩეს

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.vehicle.plate_number}'

    def price(self):
        return self.vehicle.vehicle_type.price

    def type(self):
        return self.vehicle.vehicle_type.type

    def earned(self):
        return self.vehicle.vehicle_type.price * self.washer.order_percent / 100


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
