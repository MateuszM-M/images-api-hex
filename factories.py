import factory
from app.models import Image, Thumbnail, Tier, Upload, User
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()
User = get_user_model()




class BasicTier(factory.django.DjangoModelFactory):
    class Meta:
        model = Tier

    name = "Basic"
    is_original_allowed = False
    is_expiring_allowed = False
    

class PremiumTier(factory.django.DjangoModelFactory):
    class Meta:
        model = Tier

    name = "Premium"
    is_original_allowed = True
    is_expiring_allowed = False
    

class EnterpriseTier(factory.django.DjangoModelFactory):
    class Meta:
        model = Tier

    name = "Enterprise"
    is_original_allowed = True
    is_expiring_allowed = True
    

class ThumbnailTierb(factory.django.DjangoModelFactory):
    class Meta:
        model = Thumbnail

    max_height = 200
    tier = factory.SubFactory(BasicTier)
    

class ThumbnailTierp(factory.django.DjangoModelFactory):
    class Meta:
        model = Thumbnail

    max_height = 200
    tier = factory.SubFactory(PremiumTier)
    

class ThumbnailTierpp(factory.django.DjangoModelFactory):
    class Meta:
        model = Thumbnail

    max_height = 400
    tier = factory.SubFactory(PremiumTier)
    

class ThumbnailTiere(factory.django.DjangoModelFactory):
    class Meta:
        model = Thumbnail

    max_height = 200
    tier = factory.SubFactory(EnterpriseTier)
    

class ThumbnailTieree(factory.django.DjangoModelFactory):
    class Meta:
        model = Thumbnail

    max_height = 400
    tier = factory.SubFactory(EnterpriseTier)


class BasicUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()
    password = factory.PostGenerationMethodCall(
        'set_password', 'BasicPass1!')
    

class PremiumUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()
    password = factory.PostGenerationMethodCall(
        'set_password', 'PremiumPass1!')
    

class EnterpriseUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()
    password = factory.PostGenerationMethodCall(
        'set_password', 'EnterprisePass1!')
    


