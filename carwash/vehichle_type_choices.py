from django.db.models import IntegerChoices


class VehicleTypeChoices(IntegerChoices):
    Sedan = 1
    Coupe = 2
    Jeep = 3
    HATCHBACK = 4
    WAGON = 5
    SUV = 6
    MINIVAN = 7
    PICKUP = 8
