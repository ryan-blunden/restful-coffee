from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from customers.models import Customer


@receiver(post_save, sender=Customer)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance.user)
