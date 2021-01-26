from django.db.models import TextChoices


class VipStatusChoices(TextChoices):
    Bronze = 'Bronze'
    Silver = 'Silver'
    Gold = 'Gold'
    Platinum = 'Platinum'
    Diamond = 'Diamond'
