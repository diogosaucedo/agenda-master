from django.contrib import admin
from schedule.models import Schedule


# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    ...


admin.site.register(Schedule, ScheduleAdmin)
