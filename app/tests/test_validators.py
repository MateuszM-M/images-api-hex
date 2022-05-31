import pytest
from app.validators import (validate_max_duration, validate_max_height,
                       validate_min_duration)

from django.core.exceptions import ValidationError

def test_validate_valid_max_height():
    valid = validate_max_height(950)
    assert valid == 950

    
def test_validate_invalid_max_height():
    with pytest.raises(ValidationError) as ve:
        validate_max_height(1050)
    assert ve.value.args[0] == "Maximum thumbnail height is 1000px."