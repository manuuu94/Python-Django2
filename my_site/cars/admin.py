from django.contrib import admin
from .models import Car,Review
# Register your models here.

''' changes the order of the fields in the admin site
class CarAdmin(admin.ModelAdmin):
    fields = ['brand','year']

### registers the model with the customized admin view
admin.site.register(Car,CarAdmin)
'''

#create a more customized model in the admin site for this model. 
class CarAdmin(admin.ModelAdmin):
    fieldsets = [("TIME",{'fields':['year']}),
                 ("INFO",{'fields':['brand']})
                ]

admin.site.register(Car,CarAdmin)


#just registers the model with a simple default view

#admin.site.register(Car)

admin.site.register(Review)







