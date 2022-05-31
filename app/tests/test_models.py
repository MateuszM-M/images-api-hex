import pytest

from app.models import Image, Thumbnail, Tier, Upload, User

def test_tier_str(db, basic_tier1):
    assert basic_tier1.__str__() == basic_tier1.name
    
def test_thumnbail_str(db, basic_thumbnail1):
    assert basic_thumbnail1.__str__() == f"{basic_thumbnail1.tier}: max_height: {basic_thumbnail1.max_height}"