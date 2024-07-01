from django.contrib import admin
from .models import User, Bicycle, RentalHistory

admin.site.register(User)
admin.site.register(Bicycle)
admin.site.register(RentalHistory)