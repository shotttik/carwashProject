from django.core.exceptions import ValidationError


def validate_plate_number(value):
    if value.isdigit():
        raise ValidationError("Please input plate number correctly. ex `AB123CD`")


def validate_manufacturer(value):
    symbols = ['<', ',', '>', '.', '?', '/', '|', "'", ':', ';', '}', ']', '{', '[', ')', '(', '*', '&', '^', '%', '$',
               '#', '@', '!', '~', '`']
    if symbols in value:
        raise ValidationError("Please Input Manufacturer Correctly")
