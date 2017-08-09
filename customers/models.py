from django.contrib.auth.models import User
from django.db import models

from coffeerest.models import BaseModel


class Customer(BaseModel):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['date_created']

    @property
    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Location(BaseModel):
    customer = models.ForeignKey(Customer)
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return '{} {},{}'.format(self.customer.full_name, self.lattitude, self.longitude)

    class Meta:
        ordering = ['date_created']
