from django.contrib import admin

# Register your models here.
from . models import Carlist,Showroom,Review
admin.site.register(Carlist)
admin.site.register(Showroom)
admin.site.register(Review)
