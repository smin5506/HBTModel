from django.contrib import admin
from .models import HBT

# Register your models here.
admin.site.register(HBT.Head)
admin.site.register(HBT.Body)
admin.site.register(HBT.Tail)