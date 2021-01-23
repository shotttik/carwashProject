from django.db import models
from .vehichle_type_choices import VehicleTypeChoices


class CardModel(models.Model):
    vip = models.CharField(verbose_name='Vip Status', max_length=255)
    limit = models.PositiveSmallIntegerField(verbose_name='Day limit', default=0)

    def __str__(self):
        return self.vip

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class ClientModel(models.Model):
    type = models.PositiveSmallIntegerField("Vehicle Type", choices=VehicleTypeChoices.choices,
                                            default=VehicleTypeChoices.Sedan)
    plate_number = models.CharField(max_length=11, unique=True)
    discount_card = models.ForeignKey('carwash.CardModel', on_delete=models.PROTECT)

    def __str__(self):
        return self.plate_number

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class WasherModel(models.Model):
    full_name = models.CharField(verbose_name='Full name', max_length=255, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', default=0)
    phone = models.CharField(verbose_name='Mobile phone number', max_length=9, unique=True)
    order = models.OneToOneField('carwash.ClientModel', on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Washer'
        verbose_name_plural = 'Washers'


class Administrator(models.Model):
    full_name = models.CharField(verbose_name='Full Name', max_length=255, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Age', default=0)
    personal_number = models.CharField(max_length=11, unique=True)
    locations = models.ManyToManyField(to='carwash.Location', through='AdministratorLocation')

    def __str__(self):
        return self.full_name


class Location(models.Model):
    adress = models.CharField(verbose_name='Adress', max_length=255)
    administrators = models.ManyToManyField(to='carwash.Administrator', through='AdministratorLocation')

    def __str__(self):
        return self.adress


class AdministratorLocation(models.Model):
    administrator = models.ForeignKey(to='carwash.Administrator', on_delete=models.CASCADE)
    location = models.ForeignKey(to='carwash.Location', on_delete=models.CASCADE)
