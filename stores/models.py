from django.db import models

from coffeerest.models import BaseModel
from customers.models import Customer


class Store(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']


class Order(BaseModel):
    store = models.ForeignKey(Store)
    customer = models.ForeignKey(Customer)
    coffee = models.CharField(max_length=100)
    expires = models.DateTimeField(blank=True, default=None)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return '{}, {} {}'.format(self.store, self.customer, self.coffee)

    class Meta:
        ordering = ['date_created']
