from django.db import models
from carwash.vehichle_type_choices import VehicleTypeChoices


class VehicleType(models.Model):
    type = models.CharField(max_length=255, verbose_name="Vehicle Type",
                            choices=VehicleTypeChoices.choices,
                            default=VehicleTypeChoices.SEDAN, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Price $")

    def __str__(self):
        return f'{self.type}'


class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=255, verbose_name="Manufacturer")
    model = models.CharField(max_length=255, verbose_name='Model')
    plate_number = models.CharField(max_length=15, verbose_name='Plate Number')
    vehicle_type = models.ForeignKey(to='carwash.VehicleType', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.vehicle_type}'

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Order(models.Model):
    vehicle = models.ForeignKey(to="carwash.Vehicle", on_delete=models.PROTECT, related_name='orders')
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Price', default=0)
    order_date = models.DateTimeField("Order date")
    completion_date = models.DateTimeField("Completion date")
    washer = models.ForeignKey(to="user.User", on_delete=models.SET_NULL, null=True, related_name='orders')
    earned = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Earned", default=0)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.vehicle.plate_number

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.vehicle.vehicle_type.price
            self.earned = self.vehicle.vehicle_type.price * self.washer.percent_per_order / 100
        super(Order, self).save(*args, **kwargs)
