from django.db.models import IntegerChoices


class VehicleTypeChoices(IntegerChoices):
    Sedan = 1
    Coupe = 2
    Jeep = 3
