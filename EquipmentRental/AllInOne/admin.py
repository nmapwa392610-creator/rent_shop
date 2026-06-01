from django.contrib import admin
from .models import Equipment,Customer,Rental
# Register your models here.
admin.site.register(Equipment)
admin.site.register(Customer)
admin.site.register(Rental)