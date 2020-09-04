from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Station)
admin.site.register(System)
admin.site.register(Type)
admin.site.register(Device)
admin.site.register(SystemType)

