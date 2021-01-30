from django.db.models import IntegerChoices


class Status(IntegerChoices):
    customer = 1, "Customer"
    washer = 2, "Washer"
    manager = 3, "Manager"
