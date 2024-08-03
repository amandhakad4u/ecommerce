from django.contrib import admin
from home.models import register
from home.models import users


# Register your models here.
admin.site.register(register)
admin.site.register(users)