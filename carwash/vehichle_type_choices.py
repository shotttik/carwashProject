from django.db.models import TextChoices


class VehicleTypeChoices(TextChoices):
    SEDAN = "SEDAN"
    COUPE = "COUPE"
    JEEP = "JEEP"
    HATCHBACK = "HATCHBACK"
    WAGON = "WAGON"
    SUV = "SUV"
    MINIVAN = "MINIVAN"
    PICKUP = "PICKUP"
