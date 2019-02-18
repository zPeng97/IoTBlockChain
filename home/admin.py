from django.contrib import admin
from .models import SensorsData, LocationData


# Register your models here.
class DateAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(SensorsData, DateAdmin)
admin.site.register(LocationData)