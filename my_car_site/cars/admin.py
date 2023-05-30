from django.contrib import admin
#import the model to set as admin for superusers
from cars.models import Car
# Register your models here.

#to just register as it is:
# admin.site.register(Car)

#to further customize it:
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time information',{'fields':['year']}),
        ('Car information',{'fields':['brand']}),
    ]

admin.site.register(Car,CarAdmin)