from django.contrib import admin
from .models import Personal, Languages, Profile, WorkXP, Education, Skills, skillDetails

# Register your models here.


admin.site.register(Personal)
admin.site.register(Languages)
admin.site.register(Profile)
admin.site.register(WorkXP)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(skillDetails)



