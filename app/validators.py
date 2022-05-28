from django.core.exceptions import ValidationError


def validate_max_height(value):
    if value > 1000:
        return value
    else:
        raise ValidationError("Maximum thumbnail height is 1000px.")