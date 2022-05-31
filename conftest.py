import pytest
from django.core.management import call_command
from pytest_factoryboy import register

from factories import (BasicTier, BasicUserFactory, EnterpriseTier,
                       EnterpriseUserFactory, PremiumTier, PremiumUserFactory,
                       ThumbnailTierb, ThumbnailTierp, ThumbnailTierpp,
                       ThumbnailTiere, ThumbnailTieree)

register(BasicUserFactory)
register(ThumbnailTierb)
register(BasicTier)
register(PremiumUserFactory)
register(EnterpriseUserFactory)


@pytest.fixture
def basic_tier1(db, basic_tier):
    b_tier = basic_tier.create()
    return b_tier
    
@pytest.fixture
def basic_thumbnail1(db, thumbnail_tierb, basic_tier1):
    b_thumbnail = thumbnail_tierb.create(
        tier=basic_tier1
    )
    return b_thumbnail


@pytest.fixture
def basic_user1(db, basic_user_factory, basic_tier1):
    b_user = basic_user_factory.create(
        tier=basic_tier1
    )
    return b_user


@pytest.fixture
def premium_user1(db, premium_user_factory):
    p_user = basic_user_factory.create()
    return p_user


@pytest.fixture
def enterprise_user1(db, enterprise_user_factory):
    e_user = basic_user_factory.create()
    return e_user
