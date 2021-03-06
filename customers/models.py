from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from coffeerest.models import BaseModel


class Customer(BaseModel):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['date_created']

    @property
    def auth_token(self):
        return Token.objects.get_or_create(user=self.user)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def full_last(self):
        return self.user.last_name

    @property
    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    @property
    def email(self):
        return self.user.email


class Location(BaseModel):
    customer = models.ForeignKey(Customer)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return '{} {},{}'.format(self.customer.full_name, self.latitude, self.longitude)

    class Meta:
        ordering = ['date_created']
