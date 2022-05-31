from django.core.exceptions import ValidationError


def validate_max_height(value):
    """
    Validates max height of thumbnail.
    Max height is 1000px.
    """
    if value < 1000:
        return value
    else:
        raise ValidationError("Maximum thumbnail height is 1000px.")
    

def validate_max_duration(value):
    """
    Validates max duration.
    Max duration is 30.000 seconds.
    """
    if value <= 30000:
        return value
    else:
        raise ValidationError("Maximum duration is 30.000 seconds.")
    
    
def validate_min_duration(value):
    """
    Validates min duration.
    Min duration is 30 seconds.
    """
    if value >= 30:
        return value
    else:
        raise ValidationError("Minimum duration is 30 seconds.")