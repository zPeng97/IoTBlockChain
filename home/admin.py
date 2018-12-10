from django.contrib import admin
from .models import SensorsData


# Register your models here.
class DateAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(SensorsData, DateAdmin)
