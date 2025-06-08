from django.contrib import admin

# Register your models here.
from . models import Carlist,Showroom
admin.site.register(Carlist)
admin.site.register(Showroom)