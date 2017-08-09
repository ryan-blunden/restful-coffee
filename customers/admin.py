from django.contrib import admin

from coffeerest.admin import EnabledModelAdmin
from customers import models


@admin.register(models.Customer)
class CustomerAdmin(EnabledModelAdmin):
    list_display = ('full_name', 'deleted')
    list_filter = ('deleted',)

@admin.register(models.Location)
class LocationAdmin(EnabledModelAdmin):
    list_display = ('customer', 'latitude', 'longitude', 'date_created')
    list_filter = ('date_created',)

